"""Reference analysis utilities for Study 0.

The primary scientific unit is a resolved Forecast Contract, with cluster-level
resampling when contracts share an operational episode. This module deliberately
uses only the Python standard library.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import exp, log
from random import Random
from statistics import mean, median, pstdev
from typing import Sequence

EPS = 0.01


def clip_probability(p: float, eps: float = EPS) -> float:
    if not 0 <= p <= 1:
        raise ValueError("probability must lie in [0,1]")
    if not 0 < eps < 0.5:
        raise ValueError("eps must lie in (0,0.5)")
    return min(1 - eps, max(eps, p))


def logit(p: float, eps: float = EPS) -> float:
    p = clip_probability(p, eps)
    return log(p / (1 - p))


def logistic(x: float) -> float:
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    z = exp(x)
    return z / (1 + z)


def brier_score(p: float, y: int) -> float:
    """Normalized binary quadratic/Brier loss (p-y)^2.

    The original two-category vector form sums both category errors and is twice
    this value for a binary event. This project uses the normalized convention.
    """
    if y not in (0, 1):
        raise ValueError("binary outcome must be 0 or 1")
    if not 0 <= p <= 1:
        raise ValueError("probability must lie in [0,1]")
    return (p - y) ** 2


def log_score_loss(p: float, y: int, eps: float = EPS) -> float:
    p = clip_probability(p, eps)
    if y not in (0, 1):
        raise ValueError("binary outcome must be 0 or 1")
    return -(y * log(p) + (1 - y) * log(1 - p))


def aggregate_private(probabilities: Sequence[float]) -> tuple[float, float]:
    if not probabilities:
        raise ValueError("at least one forecast is required")
    for p in probabilities:
        if not 0 <= p <= 1:
            raise ValueError("probability must lie in [0,1]")
    return mean(probabilities), median(probabilities)


def meta_recalibrated_probability(
    probabilities: Sequence[float],
    meta_predicted_peer_means: Sequence[float],
    *,
    a: float = 2.0,
    eps: float = EPS,
) -> float:
    """Fixed shared-prior/meta-belief recalibration used as a protocol candidate.

    logit(p*) = M_bar + a * (L_bar - M_bar), where L_bar is the mean
    logit of own probabilities and M_bar is the mean logit of the participant's
    prediction of peers' average probability.

    This is a project implementation inspired by meta-belief/shared-information
    aggregation literature; it is not claimed to reproduce a published method exactly.
    """
    if len(probabilities) != len(meta_predicted_peer_means):
        raise ValueError("own and meta-prediction vectors must have equal length")
    if not probabilities:
        raise ValueError("at least one forecast is required")
    if a <= 0:
        raise ValueError("a must be positive")
    l_bar = mean(logit(p, eps) for p in probabilities)
    m_bar = mean(logit(m, eps) for m in meta_predicted_peer_means)
    return logistic(m_bar + a * (l_bar - m_bar))


def belief_dispersion(probabilities: Sequence[float], eps: float = EPS) -> float:
    if len(probabilities) < 2:
        raise ValueError("belief dispersion is undefined for fewer than two forecasts")
    return pstdev(logit(p, eps) for p in probabilities)


def normalized_role_diversity(roles: Sequence[str], *, eligible_role_count: int) -> float:
    if not roles:
        raise ValueError("at least one role observation is required")
    observed = len(set(roles))
    if eligible_role_count < observed:
        raise ValueError("eligible_role_count cannot be smaller than observed categories")
    if eligible_role_count <= 1:
        return 0.0
    counts = Counter(roles)
    n = len(roles)
    entropy = -sum((c / n) * log(c / n) for c in counts.values())
    return entropy / log(eligible_role_count)


def brier_diversity_identity(probabilities: Sequence[float], y: int) -> tuple[float, float]:
    """Return both sides of the exact mean-forecast Brier diversity identity."""
    if not probabilities:
        raise ValueError("at least one forecast is required")
    p_bar = mean(probabilities)
    left = brier_score(p_bar, y)
    right = mean(brier_score(p, y) for p in probabilities) - mean((p - p_bar) ** 2 for p in probabilities)
    return left, right


@dataclass(frozen=True)
class ForecastEvent:
    event_id: str
    cluster_id: str
    outcome: int
    collective_probability: float
    reference_probability: float

    @property
    def delta(self) -> float:
        return brier_score(self.collective_probability, self.outcome) - brier_score(self.reference_probability, self.outcome)


def mean_paired_delta(events: Sequence[ForecastEvent]) -> float:
    if not events:
        raise ValueError("at least one event is required")
    return mean(e.delta for e in events)


def cluster_bootstrap_delta(
    events: Sequence[ForecastEvent],
    *,
    replicates: int = 10_000,
    seed: int = 20260926,
) -> tuple[float, float, float]:
    """Return point estimate and percentile 95% interval using cluster resampling."""
    if replicates <= 0:
        raise ValueError("replicates must be positive")
    grouped: dict[str, list[ForecastEvent]] = defaultdict(list)
    for event in events:
        if not event.cluster_id:
            raise ValueError("every event must have a non-empty cluster_id")
        grouped[event.cluster_id].append(event)
    cluster_ids = sorted(grouped)
    if len(cluster_ids) < 2:
        raise ValueError("cluster bootstrap requires at least two independent clusters")

    rng = Random(seed)
    boot: list[float] = []
    for _ in range(replicates):
        sampled_cluster_ids = [rng.choice(cluster_ids) for _ in cluster_ids]
        sample_events = [event for cid in sampled_cluster_ids for event in grouped[cid]]
        boot.append(mean_paired_delta(sample_events))

    boot.sort()
    lo = boot[int(0.025 * (replicates - 1))]
    hi = boot[int(0.975 * (replicates - 1))]
    return mean_paired_delta(events), lo, hi


def base_rate_skill(collective_losses: Sequence[float], base_rate_losses: Sequence[float]) -> float:
    if len(collective_losses) != len(base_rate_losses) or not collective_losses:
        raise ValueError("paired non-empty loss vectors are required")
    denominator = mean(base_rate_losses)
    if denominator == 0:
        raise ValueError("base-rate mean loss is zero; skill score undefined")
    return 1 - mean(collective_losses) / denominator
