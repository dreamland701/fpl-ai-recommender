"""Trainable baseline forecasting models."""

from __future__ import annotations

import json
import os
import warnings
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from .dataset import CanonicalDataset, WeekId, latest_training_cutoff, parse_week_id, training_rows_asof
from .types import FittedModelBundle, PlayerForecast


@dataclass
class RidgeRegressor:
    feature_names: Sequence[str]
    alpha: float = 1.0
    intercept_: float = 0.0
    coefficients_: Sequence[float] = ()
    feature_means_: Sequence[float] = ()
    feature_scales_: Sequence[float] = ()
    feature_mins_: Sequence[float] = ()
    feature_maxs_: Sequence[float] = ()
    rmse_: float = 0.0

    @staticmethod
    def _decision_weights(frame: pd.DataFrame, n_rows: int):
        """Per-row weights for the decision-weighted objective, or None when off."""
        if os.environ.get("FPL_DECISION_WEIGHTED", "0") != "1":
            return None
        column = os.environ.get("FPL_DECISION_WEIGHT_COLUMN", "minutes_avg_3")
        if column not in frame.columns:
            return None
        try:
            multiplier = float(os.environ.get("FPL_DECISION_WEIGHT_MULT", "4.0"))
            threshold = float(os.environ.get("FPL_DECISION_WEIGHT_THRESHOLD", "60.0"))
        except ValueError:
            return None
        values = pd.to_numeric(frame[column], errors="coerce").fillna(0.0).to_numpy(dtype=float)
        weights = np.where(values > threshold, multiplier, 1.0)
        if len(weights) != n_rows:
            return None
        # Keep the effective sample size fixed so alpha means the same thing
        # with weighting on as off.
        return weights * (len(weights) / weights.sum())

    @staticmethod
    def _recency_weights(frame: pd.DataFrame, n_rows: int):
        raw = os.environ.get("FPL_RECENCY_HALFLIFE", "")
        if not raw or "season" not in frame.columns:
            return None
        try:
            halflife = float(raw)
        except ValueError:
            return None
        if halflife <= 0:
            return None
        start = pd.to_numeric(frame["season"].astype(str).str.slice(0, 4), errors="coerce")
        if start.notna().sum() == 0:
            return None
        age = (start.max() - start).fillna(0.0).to_numpy(dtype=float)
        weights = 0.5 ** (age / halflife)
        if len(weights) != n_rows:
            return None
        return weights * (len(weights) / weights.sum())

    def fit(self, frame: pd.DataFrame, target_column: str) -> "RidgeRegressor":
        # A NaN label is an immature target (its horizon had not settled at the
        # training cutoff, see dataset.training_rows_asof), not a zero.
        frame = frame.loc[pd.to_numeric(frame[target_column], errors="coerce").notna()]
        if frame.empty:
            warnings.warn(f"No settled rows for {target_column}; this head will predict 0.", stacklevel=2)
            width = len(self.feature_names)
            self.intercept_ = 0.0
            self.coefficients_ = [0.0] * width
            self.feature_means_ = [0.0] * width
            self.feature_scales_ = [1.0] * width
            self.feature_mins_ = [0.0] * width
            self.feature_maxs_ = [0.0] * width
            self.rmse_ = 0.0
            return self
        x = frame[list(self.feature_names)].fillna(0.0).to_numpy(dtype=float)
        y = pd.to_numeric(frame[target_column], errors="coerce").to_numpy(dtype=float)

        means = x.mean(axis=0)
        scales = x.std(axis=0)
        scales[scales == 0] = 1.0
        x_scaled = (x - means) / scales
        x_design = np.column_stack([np.ones(len(x_scaled)), x_scaled])

        penalty = np.eye(x_design.shape[1]) * self.alpha
        penalty[0, 0] = 0.0

        # F11 (FPL_DECISION_WEIGHTED=1): weighted least squares, upweighting
        # the rows a squad decision can actually turn on.
        #
        # The shipping metric is realized squad points, but the objective is
        # plain squared error over ~600 players a week, almost none of whom
        # will ever be picked. Prototyped on this ridge before committing any
        # GPU to the adapter equivalent: weighting by whether a player is a
        # settled starter improved BOTH error and the realized points of the
        # 11 highest-forecast players (4.318 -> 5.008 per pick per week),
        # which is unusual on this project — the two normally trade off.
        #
        # `FPL_DECISION_WEIGHT_COLUMN` picks the signal (default minutes_avg_3)
        # and `FPL_DECISION_WEIGHT_MULT` the multiplier applied above its
        # threshold. Default-OFF until the three-window decision backtest says
        # otherwise.
        weights = self._decision_weights(frame, len(y))
        # Programme item 1 (2026-10-17, FPL_RECENCY_HALFLIFE=<seasons>): down-weight older seasons so the fit
        # tracks the current scoring regime (Defensive Contribution points since 2025-26 moved DEF from 2.9 to
        # 3.7 points per 90-minute appearance, MID 3.75 -> 4.0, FWD 4.6 -> 4.2). Weight halves per half-life of
        # season distance from the newest season in the frame; effective sample size stays n.
        recency = self._recency_weights(frame, len(y))
        if recency is not None:
            weights = recency if weights is None else (weights * recency) * (len(y) / (weights * recency).sum())
        if weights is None:
            coefficients = np.linalg.solve(x_design.T @ x_design + penalty, x_design.T @ y)
        else:
            weighted = x_design * weights[:, None]
            coefficients = np.linalg.solve(weighted.T @ x_design + penalty, weighted.T @ y)

        self.intercept_ = float(coefficients[0])
        self.coefficients_ = coefficients[1:].tolist()
        self.feature_means_ = means.tolist()
        self.feature_scales_ = scales.tolist()
        self.feature_mins_ = x.min(axis=0).tolist()
        self.feature_maxs_ = x.max(axis=0).tolist()

        predictions = self.predict(frame)
        self.rmse_ = float(np.sqrt(np.mean((predictions - y) ** 2)))
        return self

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        x = frame[list(self.feature_names)].fillna(0.0).to_numpy(dtype=float)
        # Clip inputs to the range observed at fit time before scoring. A
        # linear model extrapolating past its training domain can swing
        # arbitrarily (found 2026-08-12: a live player priced above any
        # price ever seen in training produced a negative raw 3GW
        # prediction, clipped to a nonsensical 0.0 for an obvious nailed
        # starter) -- clamping the input treats out-of-range values as if
        # they were at the edge of the training distribution, which is
        # the standard defensive fix for this failure mode. No-op for any
        # model loaded from an older saved JSON without mins/maxs.
        if self.feature_mins_ and self.feature_maxs_:
            mins = np.asarray(self.feature_mins_, dtype=float)
            maxs = np.asarray(self.feature_maxs_, dtype=float)
            x = np.clip(x, mins, maxs)
        means = np.asarray(self.feature_means_, dtype=float)
        scales = np.asarray(self.feature_scales_, dtype=float)
        x_scaled = (x - means) / scales
        coefficients = np.asarray(self.coefficients_, dtype=float)
        return self.intercept_ + x_scaled @ coefficients

    def to_json_dict(self) -> Dict[str, object]:
        return {
            "feature_names": list(self.feature_names),
            "alpha": self.alpha,
            "intercept": self.intercept_,
            "coefficients": list(self.coefficients_),
            "feature_means": list(self.feature_means_),
            "feature_scales": list(self.feature_scales_),
            "feature_mins": list(self.feature_mins_),
            "feature_maxs": list(self.feature_maxs_),
            "rmse": self.rmse_,
        }

    @classmethod
    def from_json_dict(cls, payload: Dict[str, object]) -> "RidgeRegressor":
        return cls(
            feature_names=payload["feature_names"],
            alpha=float(payload["alpha"]),
            intercept_=float(payload["intercept"]),
            coefficients_=payload["coefficients"],
            feature_means_=payload["feature_means"],
            feature_scales_=payload["feature_scales"],
            feature_mins_=payload.get("feature_mins", []),
            feature_maxs_=payload.get("feature_maxs", []),
            rmse_=float(payload.get("rmse", 0.0)),
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_json_dict(), indent=2))

    @classmethod
    def load(cls, path: Path) -> "RidgeRegressor":
        return cls.from_json_dict(json.loads(path.read_text()))


@dataclass
class GBMRegressor:
    """Gradient-boosted trees behind the RidgeRegressor interface (FPL_MODEL_CLASS=hgb).

    Asks whether the linear classic model misses nonlinear structure: thresholds
    (a nailed starter vs a rotation risk), interactions (form x fixture, minutes x
    price), saturation at the top. Squared-error loss, so it still targets the
    mean outcome. Missing values go to the trees natively instead of being
    zero-filled. `rmse_` is taken from a companion ridge so the reported
    forecast confidence stays comparable; it is not used by any decision.
    """

    feature_names: Sequence[str]
    alpha: float = 1.0
    rmse_: float = 0.0
    model_: object = None

    def fit(self, frame: pd.DataFrame, target_column: str) -> "GBMRegressor":
        from sklearn.ensemble import HistGradientBoostingRegressor

        frame = frame.loc[pd.to_numeric(frame[target_column], errors="coerce").notna()]
        if frame.empty:
            warnings.warn(f"No settled rows for {target_column}; this head will predict 0.", stacklevel=2)
            return self
        x = frame[list(self.feature_names)].to_numpy(dtype=float)
        y = pd.to_numeric(frame[target_column], errors="coerce").to_numpy(dtype=float)
        self.model_ = HistGradientBoostingRegressor(
            loss="squared_error",
            learning_rate=float(os.environ.get("FPL_HGB_LEARNING_RATE", "0.05")),
            max_iter=int(os.environ.get("FPL_HGB_MAX_ITER", "400")),
            max_leaf_nodes=int(os.environ.get("FPL_HGB_MAX_LEAF_NODES", "31")),
            min_samples_leaf=int(os.environ.get("FPL_HGB_MIN_SAMPLES_LEAF", "100")),
            l2_regularization=1.0,
            random_state=0,
        ).fit(x, y)
        self.rmse_ = RidgeRegressor(feature_names=self.feature_names, alpha=self.alpha).fit(frame, target_column).rmse_
        return self

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        if self.model_ is None:
            return np.zeros(len(frame))
        return self.model_.predict(frame[list(self.feature_names)].to_numpy(dtype=float))


@dataclass
class LogisticAppearance:
    """P(plays at least once) as a logistic regression on the same features (FPL_APPEARANCE_LOGISTIC=1,
    2026-10-14, review item P1-02). The default P(appear) is predicted minutes / 90, a ratio of a
    regression output; a classifier fitted on the appearance label is the direct estimate the
    threshold/soft availability rules and the chip pricing actually want."""

    feature_names: Sequence[str]
    c: float = 1.0
    intercept_: float = 0.0
    coefficients_: Sequence[float] = ()
    feature_means_: Sequence[float] = ()
    feature_scales_: Sequence[float] = ()

    def fit(self, frame: pd.DataFrame, target_column: str = "label_appearance_probability") -> "LogisticAppearance":
        from sklearn.linear_model import LogisticRegression

        x = frame[list(self.feature_names)].fillna(0.0).to_numpy(dtype=float)
        y = (pd.to_numeric(frame[target_column], errors="coerce").fillna(0.0).to_numpy(dtype=float) > 0.5).astype(int)
        means = x.mean(axis=0); scales = x.std(axis=0); scales[scales == 0] = 1.0
        if y.min() == y.max():
            self.intercept_ = 20.0 if y.max() == 1 else -20.0
            self.coefficients_ = [0.0] * x.shape[1]
        else:
            model = LogisticRegression(C=self.c, max_iter=2000).fit((x - means) / scales, y)
            self.intercept_ = float(model.intercept_[0]); self.coefficients_ = model.coef_[0].tolist()
        self.feature_means_ = means.tolist(); self.feature_scales_ = scales.tolist()
        return self

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        x = frame[list(self.feature_names)].fillna(0.0).to_numpy(dtype=float)
        z = ((x - np.array(self.feature_means_)) / np.array(self.feature_scales_)) @ np.array(self.coefficients_) + self.intercept_
        return 1.0 / (1.0 + np.exp(-np.clip(z, -30.0, 30.0)))

    def save(self, path: Path) -> None:
        Path(path).write_text(json.dumps({"feature_names": list(self.feature_names), "c": self.c, "intercept": self.intercept_,
                                          "coefficients": list(self.coefficients_), "feature_means": list(self.feature_means_),
                                          "feature_scales": list(self.feature_scales_)}))

    @classmethod
    def load(cls, path: Path) -> "LogisticAppearance":
        d = json.loads(Path(path).read_text())
        return cls(feature_names=d["feature_names"], c=d["c"], intercept_=d["intercept"], coefficients_=d["coefficients"],
                   feature_means_=d["feature_means"], feature_scales_=d["feature_scales"])


def _regressor(feature_names: Sequence[str], alpha: float, head: str):
    """FPL_MODEL_CLASS=hgb swaps the heads named in FPL_HGB_HEADS (default all four) to trees."""
    heads = os.environ.get("FPL_HGB_HEADS", "minutes,1gw,3gw,5gw").split(",")
    if os.environ.get("FPL_MODEL_CLASS", "ridge") == "hgb" and head in heads:
        return GBMRegressor(feature_names=feature_names, alpha=alpha)
    return RidgeRegressor(feature_names=feature_names, alpha=alpha)


@dataclass
class ForecastModelSuite:
    feature_names: Sequence[str]
    availability_model: RidgeRegressor
    points_1gw_model: RidgeRegressor
    points_3gw_model: RidgeRegressor
    points_5gw_model: RidgeRegressor
    # Per-price-band additive offsets ({horizon: {(lo, hi): offset}}),
    # fitted only when FPL_BAND_CALIBRATION=1. Empty dict = no-op.
    band_calibration: Dict[str, Dict[Tuple[float, float], float]] = field(default_factory=dict)
    # FPL_PER_FIXTURE=1 (2026-10-13): the minutes and 1GW heads are fitted on per-fixture labels
    # (label / fixture_count) and multiplied back by the week's fixture count at predict time.
    # Found while sizing double-gameweek chips: the heads only saw a double as an additive
    # `double_gw` flag, so regular starters who doubled were forecast 4.4 against 6.0 realised
    # (singles 2.7 vs 2.7) while their single-week forecast x2 read 6.2 — the double was priced
    # as +1, not x2, over 15 double gameweeks 2020-21 → 2025-26 (memory: fpl-dgw-pricing-defect).
    per_fixture: bool = False
    # With per_fixture, the 3GW/5GW heads are per fixture too when the frame carries the forward
    # fixture counts (dataset.fixtures_next_3/5, rate-equivalent like the labels); a table without
    # them keeps the rate-per-week heads.
    per_fixture_horizon: bool = False
    # FPL_APPEARANCE_LOGISTIC=1: a fitted classifier replaces minutes/90 as P(appear).
    appearance_model: Optional[LogisticAppearance] = None
    # FPL_MINUTES_BAND_CAL=1|unflagged (2026-10-28, the Isak case): additive offsets by band of the model's own
    # per-fixture minutes forecast, fitted leave-one-season-out on the training frame. The pooled ridge is linear in
    # its rolling minutes features, so it under-forecasts players it puts at 45-72 minutes (walk-forward: forecast
    # 67 -> realised 76 min, +0.36 +/- 0.10 pts/GW for nailed players in the 60-72 band; returners from an injury
    # blank 61 -> 79 min) and is calibrated at 86+ (memory: fpl-returner-minutes-calibration). {horizon: {(lo, hi): offset}}
    # for "minutes", "1gw", "3gw", "5gw"; "unflagged" fits and applies only to rows without a pre-deadline status flag.
    minutes_band_calibration: Dict[str, Dict[Tuple[float, float], float]] = field(default_factory=dict)
    minutes_band_unflagged_only: bool = False

    @staticmethod
    def _fixture_counts(frame: pd.DataFrame) -> np.ndarray:
        return pd.to_numeric(frame.get("fixture_count", 0), errors="coerce").fillna(0.0).to_numpy(dtype=float)

    @staticmethod
    def _fixtures_ahead(frame: pd.DataFrame, horizon: int) -> np.ndarray:
        column = f"fixtures_next_{horizon}"
        if column not in frame.columns:
            return np.full(len(frame), float(horizon))
        return pd.to_numeric(frame[column], errors="coerce").fillna(float(horizon)).to_numpy(dtype=float)

    def _band_offsets(self, horizon: str, prices: np.ndarray) -> np.ndarray:
        offsets = np.zeros(len(prices), dtype=float)
        for (lo, hi), value in (self.band_calibration.get(horizon) or {}).items():
            offsets[(prices >= lo) & (prices < hi)] = value
        return offsets

    def _minutes_band_offsets(self, horizon: str, minutes: np.ndarray) -> np.ndarray:
        offsets = np.zeros(len(minutes), dtype=float)
        for (lo, hi), value in (self.minutes_band_calibration.get(horizon) or {}).items():
            offsets[(minutes >= lo) & (minutes < hi)] = value
        return offsets

    def predict_frame(self, week_frame: pd.DataFrame) -> List[PlayerForecast]:
        working_frame = week_frame.copy()
        for feature_name in self.feature_names:
            if feature_name not in working_frame.columns:
                working_frame[feature_name] = 0.0

        fixture_counts = self._fixture_counts(working_frame)
        if self.per_fixture:
            minutes_per_fixture = np.clip(self.availability_model.predict(working_frame), 0.0, 90.0)
            predicted_minutes = np.clip(minutes_per_fixture * fixture_counts, 0.0, 180.0)
            predicted_points_1 = np.clip(self.points_1gw_model.predict(working_frame), 0.0, None) * fixture_counts
        else:
            predicted_minutes = np.clip(self.availability_model.predict(working_frame), 0.0, 180.0)
            minutes_per_fixture = predicted_minutes
            predicted_points_1 = np.clip(self.points_1gw_model.predict(working_frame), 0.0, None)
        minutes_per_fixture_raw = minutes_per_fixture.copy()
        # F16 (FPL_TEAM_NEWS_OVERRIDE=1|minutes, 2026-10-21): the Guardian's pre-deadline team-news category as a
        # multiplicative override rather than a ridge term. Pooled 2022-26 ratios vs the implied XI for players
        # with a real chance of starting (minutes_avg_5 >= 30): named sub 0.65 pts / 0.6 min, doubtful 0.6 / 0.5,
        # injured or suspended 0.03 / 0.03. The additive ridge term moved a named sub by 7 minutes and left an
        # injured player at 9 forecast minutes; this applies the ratio to minutes (and to points unless =minutes).
        override = os.environ.get("FPL_TEAM_NEWS_OVERRIDE", "0")
        team_news_factor = None
        if override != "0" and {"gn_sub", "gn_doubtful", "gn_out"} <= set(working_frame.columns):
            factor = np.ones(len(working_frame), dtype=float)
            for column, value in (("gn_sub", 0.65), ("gn_doubtful", 0.55), ("gn_out", 0.03)):
                flagged = pd.to_numeric(working_frame[column], errors="coerce").fillna(0.0).to_numpy(dtype=float) >= 1.0
                factor = np.where(flagged, value, factor)
            minutes_per_fixture = minutes_per_fixture * factor
            predicted_minutes = predicted_minutes * factor
            if override != "minutes":
                predicted_points_1 = predicted_points_1 * factor
                team_news_factor = factor
        predicted_points_3 = np.clip(self.points_3gw_model.predict(working_frame), 0.0, None)
        predicted_points_5 = np.clip(self.points_5gw_model.predict(working_frame), 0.0, None)
        rate_5gw = predicted_points_5.copy() if self.per_fixture_horizon else predicted_points_5 / 5.0  # item 2
        if self.per_fixture_horizon:
            predicted_points_3 = predicted_points_3 * self._fixtures_ahead(working_frame, 3)
            predicted_points_5 = predicted_points_5 * self._fixtures_ahead(working_frame, 5)

        if team_news_factor is not None:  # this week's information only: a third / a fifth of the multi-week heads
            predicted_points_3 = predicted_points_3 * (1.0 + (team_news_factor - 1.0) / 3.0)
            predicted_points_5 = predicted_points_5 * (1.0 + (team_news_factor - 1.0) / 5.0)
        if self.minutes_band_calibration:
            band_rows = np.ones(len(working_frame), dtype=bool)
            if self.minutes_band_unflagged_only and "status_flag_pre_deadline" in working_frame.columns:
                band_rows = pd.to_numeric(working_frame["status_flag_pre_deadline"], errors="coerce").fillna(0.0).to_numpy(dtype=float) < 1.0
            mult = np.where(self.per_fixture, np.maximum(fixture_counts, 0.0), 1.0)
            off_min = self._minutes_band_offsets("minutes", minutes_per_fixture) * mult * band_rows
            predicted_minutes = np.clip(predicted_minutes + off_min, 0.0, 180.0)
            minutes_per_fixture = np.clip(minutes_per_fixture + self._minutes_band_offsets("minutes", minutes_per_fixture) * band_rows, 0.0, 90.0) if self.per_fixture else predicted_minutes
            predicted_points_1 = np.clip(predicted_points_1 + self._minutes_band_offsets("1gw", minutes_per_fixture_raw) * mult * band_rows, 0.0, None)
            predicted_points_3 = np.clip(predicted_points_3 + self._minutes_band_offsets("3gw", minutes_per_fixture_raw) * band_rows, 0.0, None)
            predicted_points_5 = np.clip(predicted_points_5 + self._minutes_band_offsets("5gw", minutes_per_fixture_raw) * band_rows, 0.0, None)
        if self.band_calibration:
            prices = pd.to_numeric(
                working_frame.get("price_pre_deadline", working_frame.get("price")),
                errors="coerce",
            ).fillna(0.0).to_numpy(dtype=float)
            predicted_points_1 = np.clip(predicted_points_1 + self._band_offsets("1gw", prices), 0.0, None)
            predicted_points_3 = np.clip(predicted_points_3 + self._band_offsets("3gw", prices), 0.0, None)
            predicted_points_5 = np.clip(predicted_points_5 + self._band_offsets("5gw", prices), 0.0, None)

        if self.appearance_model is not None:
            appearance_probability = np.where(fixture_counts > 0, np.clip(self.appearance_model.predict(working_frame), 0.0, 1.0), 0.0)
        elif self.per_fixture or os.environ.get("FPL_DGW_PAPP", "0") == "1":
            # P(plays at least once), not "share of the week's possible minutes": the old ratio
            # read a nailed starter's double gameweek as 100/180 = 0.56 (0.84 the week before),
            # and the soft-availability optimizer then discounted every doubler (fpl-dgw-pricing-defect).
            appearance_probability = np.where(
                fixture_counts > 0, np.clip(minutes_per_fixture / 90.0, 0.0, 1.0), 0.0
            )
        else:
            appearance_probability = np.clip(
                predicted_minutes / np.maximum(90.0 * working_frame["fixture_count"].clip(lower=1).to_numpy(dtype=float), 1.0),
                0.0,
                1.0,
            )
        uncertainty = np.clip(
            (self.points_3gw_model.rmse_ + self.availability_model.rmse_ / 90.0) / np.maximum(predicted_points_3, 1.0),
            0.05,
            1.0,
        )

        forecasts = []
        for idx, record in enumerate(working_frame.to_dict(orient="records")):
            price = record.get("price_pre_deadline", record.get("price", 0.0))
            forecasts.append(
                PlayerForecast(
                    season=str(record["season"]),
                    week=int(record["week"]),
                    player_id=int(record["player_id"]),
                    player_name=str(record["player_name"]),
                    team_id=int(record["team_id"]),
                    position=str(record["position"]),
                    price=float(price or 0.0),
                    predicted_minutes=float(predicted_minutes[idx]),
                    predicted_points_1gw=float(predicted_points_1[idx]),
                    predicted_points_3gw=float(predicted_points_3[idx]),
                    predicted_points_5gw=float(predicted_points_5[idx]),
                    appearance_probability=float(appearance_probability[idx]),
                    fixture_count=int(record.get("fixture_count", 0)),
                    uncertainty=float(uncertainty[idx]),
                    rate_5gw=float(rate_5gw[idx]),
                )
            )
        return forecasts

    def predict_week(self, dataset: CanonicalDataset, week_id: WeekId) -> List[PlayerForecast]:
        return self.predict_frame(dataset.week_frame(week_id))


PRICE_BANDS = ((0.0, 5.0), (5.0, 6.5), (6.5, 8.5), (8.5, 11.5), (11.5, 99.0))
_CALIBRATION_MIN_ROWS = 25
_CALIBRATION_TRAILING_WEEKS = 10
_CALIBRATION_OFFSET_BOUNDS = (-1.5, 2.5)


def _fit_band_calibration(
    train_frame: pd.DataFrame, suite: ForecastModelSuite
) -> Dict[str, Dict[Tuple[float, float], float]]:
    """Per-price-band additive offsets from trailing-weeks residuals.

    A pooled ridge regresses extremes toward the mean: on the E11 GW35-38
    holdout the £8.5-11.4 band realized 5.64 pts/GW against a 4.07
    prediction (the Haaland exclusion, GW2 2026-27). The offset is the
    trailing mean(label - prediction) per band per horizon, clamped, and
    only fitted where the band has enough rows. In-sample residuals are
    acceptable because the compression is model-class bias rather than
    overfit; the walk-forward backtest is the arbiter of net effect.
    """
    week_keys = sorted(
        {(s, int(w)) for s, w in zip(train_frame["season"], train_frame["week"])}
    )[-_CALIBRATION_TRAILING_WEEKS:]
    keys = set(week_keys)
    mask_recent = [
        (s, int(w)) in keys for s, w in zip(train_frame["season"], train_frame["week"])
    ]
    recent = train_frame.loc[mask_recent].copy()
    prior = train_frame.loc[[not m for m in mask_recent]]
    if recent.empty or len(prior) < 1000:
        return {}
    # Shadow refit on pre-trailing data so residuals are OUT-OF-SAMPLE for
    # the trailing weeks — in-sample residuals understate the compression
    # (measured: premium 1gw offset ~0 in-sample vs -1.56 held-out).
    shadow = {
        horizon: RidgeRegressor(
            feature_names=suite.feature_names, alpha=suite.points_1gw_model.alpha
        ).fit(prior, f"label_points_{horizon}")
        for horizon in ("1gw", "3gw", "5gw")
    }
    price = pd.to_numeric(
        recent.get("price_pre_deadline", recent.get("price")), errors="coerce"
    ).fillna(0.0)
    calibration: Dict[str, Dict[Tuple[float, float], float]] = {}
    for horizon, model in (
        ("1gw", shadow["1gw"]),
        ("3gw", shadow["3gw"]),
        ("5gw", shadow["5gw"]),
    ):
        label = pd.to_numeric(recent[f"label_points_{horizon}"], errors="coerce")
        predicted = pd.Series(model.predict(recent), index=recent.index).clip(lower=0.0)
        if horizon == "1gw" and suite.per_fixture:
            predicted = predicted * suite._fixture_counts(recent)
        elif suite.per_fixture_horizon:
            predicted = predicted * suite._fixtures_ahead(recent, int(horizon[0]))
        residual = label - predicted
        offsets: Dict[Tuple[float, float], float] = {}
        for lo, hi in PRICE_BANDS:
            band_mask = (price >= lo) & (price < hi) & residual.notna()
            if int(band_mask.sum()) < _CALIBRATION_MIN_ROWS:
                continue
            offset = float(residual[band_mask].mean())
            offsets[(lo, hi)] = min(
                max(offset, _CALIBRATION_OFFSET_BOUNDS[0]), _CALIBRATION_OFFSET_BOUNDS[1]
            )
        calibration[horizon] = offsets
    return calibration


POSITION_GROUPS = ("GK", "DEF", "MID", "FWD")
MIN_POSITION_ROWS = 500


@dataclass
class PositionRoutedSuite:
    """FPL_PER_POSITION=1 (2026-10-14): one ForecastModelSuite per position, the pooled suite as fallback.

    The pooled ridge is a single linear function for goalkeepers, defenders, midfielders and forwards,
    so a clean-sheet or goals-conceded signal cannot matter for a defender without mattering for a
    forward (the F5 clean-sheet features died in that pooled fit). Separate fits let each position
    weight its own scoring sources. Same predict_frame interface; the backtest and live paths only
    call that."""

    feature_names: Sequence[str]
    suites: Dict[str, ForecastModelSuite]
    fallback: ForecastModelSuite

    @property
    def per_fixture(self) -> bool:
        return self.fallback.per_fixture

    @property
    def per_fixture_horizon(self) -> bool:
        return self.fallback.per_fixture_horizon

    @property
    def appearance_model(self):
        return self.fallback.appearance_model

    @property
    def availability_model(self):
        return self.fallback.availability_model

    @property
    def points_1gw_model(self):
        return self.fallback.points_1gw_model

    @property
    def points_3gw_model(self):
        return self.fallback.points_3gw_model

    @property
    def points_5gw_model(self):
        return self.fallback.points_5gw_model

    def predict_frame(self, week_frame: pd.DataFrame) -> List[PlayerForecast]:
        positions = week_frame["position"].astype(str).to_numpy() if "position" in week_frame.columns else np.array([""] * len(week_frame))
        out: List[Optional[PlayerForecast]] = [None] * len(week_frame)
        for group in set(positions):
            mask = np.where(positions == group)[0]
            suite = self.suites.get(group, self.fallback)
            for idx, forecast in zip(mask, suite.predict_frame(week_frame.iloc[mask])):
                out[idx] = forecast
        return [f for f in out if f is not None]


def fit_model_suite_from_frame(
    train_frame: pd.DataFrame,
    feature_names: Sequence[str],
    alpha: float = 1.0,
):
    """The pooled suite, or (FPL_PER_POSITION=1) a position-routed suite of per-position fits."""
    pooled = _fit_single_suite(train_frame, feature_names, alpha)
    if os.environ.get("FPL_PER_POSITION", "0") not in ("1", "points") or "position" not in train_frame.columns:
        return pooled
    suites: Dict[str, ForecastModelSuite] = {}
    for group in POSITION_GROUPS:
        rows = train_frame.loc[train_frame["position"].astype(str) == group]
        if len(rows) >= MIN_POSITION_ROWS:
            suites[group] = _fit_single_suite(rows, feature_names, alpha)
            # FPL_PER_POSITION=points: position-specific points heads, pooled minutes / P(appear)
            if os.environ.get("FPL_PER_POSITION") == "points":
                suites[group].availability_model = pooled.availability_model
                suites[group].appearance_model = pooled.appearance_model
    return PositionRoutedSuite(feature_names=list(feature_names), suites=suites, fallback=pooled)


def _fit_single_suite(
    train_frame: pd.DataFrame,
    feature_names: Sequence[str],
    alpha: float = 1.0,
) -> ForecastModelSuite:
    per_fixture = os.environ.get("FPL_PER_FIXTURE", "0") == "1"
    if per_fixture:
        # Minutes and 1GW points per fixture; blank weeks (fixture_count 0, label 0) carry no
        # per-fixture information and are dropped from these two heads. 3GW/5GW labels are
        # forward sums over weeks whose fixture counts are not features, so they are unchanged.
        counts = ForecastModelSuite._fixture_counts(train_frame)
        single = train_frame.loc[counts >= 1].copy()
        single_counts = counts[counts >= 1]
        single["label_minutes_1gw"] = pd.to_numeric(single["label_minutes_1gw"], errors="coerce") / single_counts
        single["label_points_1gw"] = pd.to_numeric(single["label_points_1gw"], errors="coerce") / single_counts
        availability_model = _regressor(feature_names, alpha, "minutes").fit(single, "label_minutes_1gw")
        points_1gw_model = _regressor(feature_names, alpha, "1gw").fit(single, "label_points_1gw")
    else:
        availability_model = _regressor(feature_names, alpha, "minutes").fit(train_frame, "label_minutes_1gw")
        points_1gw_model = _regressor(feature_names, alpha, "1gw").fit(train_frame, "label_points_1gw")
    per_fixture_horizon = (per_fixture and {"fixtures_next_3", "fixtures_next_5"} <= set(train_frame.columns)
                           and os.environ.get("FPL_PER_FIXTURE_HORIZON", "1") == "1")  # =0: 1GW/minutes only (A/B)
    if per_fixture_horizon:
        horizon_models = {}
        for horizon in (3, 5):
            ahead = ForecastModelSuite._fixtures_ahead(train_frame, horizon)
            rows = train_frame.loc[ahead > 0].copy()
            rows[f"label_points_{horizon}gw"] = pd.to_numeric(rows[f"label_points_{horizon}gw"], errors="coerce") / ahead[ahead > 0]
            horizon_models[horizon] = _regressor(feature_names, alpha, f"{horizon}gw").fit(rows, f"label_points_{horizon}gw")
        points_3gw_model, points_5gw_model = horizon_models[3], horizon_models[5]
    else:
        points_3gw_model = _regressor(feature_names, alpha, "3gw").fit(train_frame, "label_points_3gw")
        points_5gw_model = _regressor(feature_names, alpha, "5gw").fit(train_frame, "label_points_5gw")
    suite = ForecastModelSuite(
        feature_names=list(feature_names),
        availability_model=availability_model,
        points_1gw_model=points_1gw_model,
        points_3gw_model=points_3gw_model,
        points_5gw_model=points_5gw_model,
        per_fixture=per_fixture,
        per_fixture_horizon=per_fixture_horizon,
    )
    if os.environ.get("FPL_APPEARANCE_LOGISTIC", "0") == "1" and "label_appearance_probability" in train_frame.columns:
        counts = ForecastModelSuite._fixture_counts(train_frame)
        suite.appearance_model = LogisticAppearance(feature_names=list(feature_names)).fit(train_frame.loc[counts >= 1])
    if os.environ.get("FPL_BAND_CALIBRATION", "0") == "1":
        suite.band_calibration = _fit_band_calibration(train_frame, suite)
    mode = os.environ.get("FPL_MINUTES_BAND_CAL", "0")
    if mode != "0":
        suite.minutes_band_unflagged_only = mode == "unflagged"
        suite.minutes_band_calibration = _fit_minutes_band_calibration(train_frame, suite, unflagged_only=suite.minutes_band_unflagged_only)
        if mode == "low":  # only the under-forecast bands below 80 min; the walk-forward 86+ band of nailed players is calibrated
            suite.minutes_band_calibration = {h: {k: v for k, v in t.items() if k[0] < 80.0} for h, t in suite.minutes_band_calibration.items()}
    return suite


_MINUTES_BANDS = [(0.0, 45.0), (45.0, 60.0), (60.0, 72.0), (72.0, 80.0), (80.0, 86.0), (86.0, 91.0)]


def _fit_minutes_band_calibration(train_frame: pd.DataFrame, suite: ForecastModelSuite, unflagged_only: bool = False,
                                  min_rows: int = 300, clamp: float = 1.5) -> Dict[str, Dict[Tuple[float, float], float]]:
    """Leave-one-season-out residuals of the minutes and points heads, pooled by band of the OUT-OF-SAMPLE per-fixture
    minutes forecast (so a season's rows are scored by heads that never saw it). Offsets = mean residual per band,
    clamped to +/- clamp points (minutes +/- 20); bands with < min_rows rows get 0. Price-band calibration (F2) left as is."""
    frame = train_frame.loc[ForecastModelSuite._fixture_counts(train_frame) >= 1.0].copy()
    if unflagged_only and "status_flag_pre_deadline" in frame.columns:
        frame = frame.loc[pd.to_numeric(frame["status_flag_pre_deadline"], errors="coerce").fillna(0.0) < 1.0]
    seasons = sorted(frame["season"].unique())
    if len(seasons) < 3 or len(frame) < 5000:
        return {}
    feats = list(suite.feature_names); alpha = suite.points_1gw_model.alpha
    counts_all = ForecastModelSuite._fixture_counts(frame)
    keep = {"minutes": [], "1gw": [], "3gw": [], "5gw": []}; bands_of = []
    for season in seasons:
        held = frame["season"] == season
        tr, te = frame.loc[~held], frame.loc[held]
        if len(te) < 500 or len(tr) < 5000:
            continue
        c_te = ForecastModelSuite._fixture_counts(te)
        if suite.per_fixture:
            rows = tr.copy(); c_tr = ForecastModelSuite._fixture_counts(rows); ok = c_tr >= 1.0; rows = rows.loc[ok]
            rows["_m"] = pd.to_numeric(rows["label_minutes_1gw"], errors="coerce") / c_tr[ok]
            rows["_p"] = pd.to_numeric(rows["label_points_1gw"], errors="coerce") / c_tr[ok]
            m_model = RidgeRegressor(feature_names=feats, alpha=suite.availability_model.alpha).fit(rows, "_m")
            p1_model = RidgeRegressor(feature_names=feats, alpha=alpha).fit(rows, "_p")
            mpf = np.clip(m_model.predict(te), 0.0, 90.0)
            res_m = pd.to_numeric(te["label_minutes_1gw"], errors="coerce").to_numpy(dtype=float) / np.maximum(c_te, 1.0) - mpf
            res_1 = pd.to_numeric(te["label_points_1gw"], errors="coerce").to_numpy(dtype=float) / np.maximum(c_te, 1.0) - np.clip(p1_model.predict(te), 0.0, None)
        else:
            m_model = RidgeRegressor(feature_names=feats, alpha=suite.availability_model.alpha).fit(tr, "label_minutes_1gw")
            p1_model = RidgeRegressor(feature_names=feats, alpha=alpha).fit(tr, "label_points_1gw")
            mpf = np.clip(m_model.predict(te), 0.0, 90.0)
            res_m = pd.to_numeric(te["label_minutes_1gw"], errors="coerce").to_numpy(dtype=float) - mpf
            res_1 = pd.to_numeric(te["label_points_1gw"], errors="coerce").to_numpy(dtype=float) - np.clip(p1_model.predict(te), 0.0, None)
        res_h = {}
        for horizon in ("3gw", "5gw"):
            if suite.per_fixture_horizon:
                res_h[horizon] = np.full(len(te), np.nan)  # rate heads: not calibrated here
                continue
            h_model = RidgeRegressor(feature_names=feats, alpha=alpha).fit(tr, f"label_points_{horizon}")
            res_h[horizon] = pd.to_numeric(te[f"label_points_{horizon}"], errors="coerce").to_numpy(dtype=float) - np.clip(h_model.predict(te), 0.0, None)
        bands_of.append(mpf); keep["minutes"].append(res_m); keep["1gw"].append(res_1); keep["3gw"].append(res_h["3gw"]); keep["5gw"].append(res_h["5gw"])
    if not bands_of:
        return {}
    band = np.concatenate(bands_of)
    out: Dict[str, Dict[Tuple[float, float], float]] = {}
    for horizon, parts in keep.items():
        res = np.concatenate(parts); table = {}
        for lo, hi in _MINUTES_BANDS:
            sel = (band >= lo) & (band < hi) & np.isfinite(res)
            if sel.sum() >= min_rows:
                lim = 20.0 if horizon == "minutes" else clamp * (1.0 if horizon == "1gw" else 3.0 if horizon == "3gw" else 5.0)
                table[(lo, hi)] = float(np.clip(res[sel].mean(), -lim, lim))
        out[horizon] = table
    return out


def train_model_suite(
    dataset: CanonicalDataset,
    model_dir: Path,
    alpha: float = 1.0,
) -> FittedModelBundle:
    model_dir = Path(model_dir)
    cutoff_season, cutoff_week = latest_training_cutoff(dataset.training_frame)
    eligible_frame = training_rows_asof(dataset.training_frame, cutoff_season, cutoff_week)
    feature_names = dataset.feature_columns

    model_suite = fit_model_suite_from_frame(
        eligible_frame,
        feature_names=feature_names,
        alpha=alpha,
    )
    availability_model = model_suite.availability_model
    points_1gw_model = model_suite.points_1gw_model
    points_3gw_model = model_suite.points_3gw_model
    points_5gw_model = model_suite.points_5gw_model

    availability_path = model_dir / "availability_minutes.json"
    points_1gw_path = model_dir / "points_1gw.json"
    points_3gw_path = model_dir / "points_3gw.json"
    points_5gw_path = model_dir / "points_5gw.json"
    availability_model.save(availability_path)
    points_1gw_model.save(points_1gw_path)
    points_3gw_model.save(points_3gw_path)
    points_5gw_model.save(points_5gw_path)
    appearance_path = None
    if model_suite.appearance_model is not None:
        appearance_path = model_dir / "appearance_logistic.json"
        model_suite.appearance_model.save(appearance_path)

    manifest = FittedModelBundle(
        feature_names=list(feature_names),
        availability_path=str(availability_path),
        points_1gw_path=str(points_1gw_path),
        points_3gw_path=str(points_3gw_path),
        points_5gw_path=str(points_5gw_path),
        per_fixture=model_suite.per_fixture,
        per_fixture_horizon=model_suite.per_fixture_horizon,
        appearance_path=str(appearance_path) if appearance_path else None,
    )
    (model_dir / "manifest.json").write_text(json.dumps(asdict(manifest), indent=2))
    return manifest


def load_model_suite(model_dir: Path) -> ForecastModelSuite:
    model_dir = Path(model_dir)
    manifest = json.loads((model_dir / "manifest.json").read_text())
    feature_names = manifest["feature_names"]
    return ForecastModelSuite(
        feature_names=feature_names,
        availability_model=RidgeRegressor.load(Path(manifest["availability_path"])),
        points_1gw_model=RidgeRegressor.load(Path(manifest["points_1gw_path"])),
        points_3gw_model=RidgeRegressor.load(Path(manifest["points_3gw_path"])),
        points_5gw_model=RidgeRegressor.load(Path(manifest["points_5gw_path"])),
        per_fixture=bool(manifest.get("per_fixture", False)),
        per_fixture_horizon=bool(manifest.get("per_fixture_horizon", False)),
        appearance_model=LogisticAppearance.load(Path(manifest["appearance_path"])) if manifest.get("appearance_path") else None,
    )
