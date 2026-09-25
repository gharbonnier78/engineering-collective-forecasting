"""Reference analysis utilities for Study 0.

No external dependencies. This module intentionally implements only the frozen core
statistics needed for protocol replay; richer exploratory analysis belongs in separate,
clearly labelled notebooks or scripts.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import log
from random import Random
from statistics import mean, median, pstdev
from typing import Iterable, Sequence

EPS = 0.01


def clip_probability(p: float, eps: float = EPS) -> float:
    if not 0 <= p <= 1:
        raise ValueError("probability must lie in [0,1]")
    return min(1 - eps, max(eps, p))


def brier_score(p: float, y: int) -> float:
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


def belief_dispersion(probabilities: Sequence[float], eps: float = EPS) -> float:
    if len(probabilities) < 2:
        return 0.0
    logits = []
    for p in probabilities:
        p = clip_probability(p, eps)
        logits.append(log(p / (1 - p)))
    return pstdev(logits)


def normalized_role_diversity(roles: Sequence[str], eligible_role_count: int | None = None) -> float:
    if not roles:
        return 0.0
    counts = Counter(roles)
    denom_categories = eligible_role_count or len(counts)
    if denom_categories <= 1:
        return 0.0
    n = len(roles)
    entropy = -sum((c / n) * log(c / n) for c in counts.values())
    return entropy / log(denom_categories)


@dataclass(frozen=True)
class PairedEvent:
    event_id: str
    cluster_id: str
    outcome: int
    market_probability: float
    mean_probability: float

    @property
    def delta(self) -> float:
        return brier_score(self.market_probability, self.outcome) - brier_score(self.mean_probability, self.outcome)


def mean_paired_delta(events: Sequence[PairedEvent]) -> float:
    if not events:
        raise ValueError("at least one event is required")
    return mean(e.delta for e in events)


def cluster_bootstrap_delta(
    events: Sequence[PairedEvent],
    *,
    replicates: int = 10_000,
    seed: int = 20260925,
) -> tuple[float, float, float]:
    """Return point estimate and percentile 95% bootstrap interval.

    Resampling occurs at cluster level. When a cluster is sampled, all its events are
    included, preserving within-cluster dependence rather than pseudo-replicating events.
    """
    if replicates <= 0:
        raise ValueError("replicates must be positive")
    grouped: dict[str, list[PairedEvent]] = defaultdict(list)
    for event in events:
        grouped[event.cluster_id].append(event)
    cluster_ids = sorted(grouped)
    if not cluster_ids:
        raise ValueError("at least one cluster is required")
    rng = Random(seed)
    boot = []
    for _ in range(replicates):
        sampled = [rng.choice(cluster_ids) for _ in cluster_ids]
        sample_events = [event for cid in sampled for event in grouped[cid]]
        boot.append(mean_paired_delta(sample_events))
    boot.sort()
    lo = boot[int(0.025 * (replicates - 1))]
    hi = boot[int(0.975 * (replicates - 1))]
    return mean_paired_delta(events), lo, hi
