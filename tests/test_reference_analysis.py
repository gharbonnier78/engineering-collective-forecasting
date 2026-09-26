import unittest

from analysis.reference_analysis import (
    ForecastEvent,
    aggregate_private,
    belief_dispersion,
    brier_diversity_identity,
    brier_score,
    cluster_bootstrap_delta,
    meta_recalibrated_probability,
    normalized_role_diversity,
)


class ReferenceAnalysisTests(unittest.TestCase):
    def test_brier_normalized_binary_convention(self):
        self.assertAlmostEqual(brier_score(0.8, 1), 0.04)
        self.assertAlmostEqual(brier_score(0.2, 0), 0.04)

    def test_private_aggregation(self):
        avg, med = aggregate_private([0.2, 0.5, 0.8])
        self.assertAlmostEqual(avg, 0.5)
        self.assertAlmostEqual(med, 0.5)

    def test_meta_recalibration_equal_own_and_meta_returns_same_logit_center(self):
        p = meta_recalibrated_probability([0.6, 0.6], [0.6, 0.6], a=2.0)
        self.assertAlmostEqual(p, 0.6)

    def test_belief_dispersion_requires_two_forecasters(self):
        with self.assertRaises(ValueError):
            belief_dispersion([0.5])

    def test_belief_dispersion_zero_when_equal(self):
        self.assertAlmostEqual(belief_dispersion([0.5, 0.5]), 0.0)

    def test_role_diversity_uses_eligible_taxonomy(self):
        observed = normalized_role_diversity(["dev", "test"], eligible_role_count=9)
        self.assertAlmostEqual(observed, 0.31546487678572877)

    def test_brier_diversity_identity(self):
        left, right = brier_diversity_identity([0.2, 0.5, 0.8], 1)
        self.assertAlmostEqual(left, right)

    def test_cluster_bootstrap_requires_two_clusters(self):
        events = [ForecastEvent("e1", "c1", 1, 0.8, 0.6)]
        with self.assertRaises(ValueError):
            cluster_bootstrap_delta(events, replicates=100, seed=1)

    def test_cluster_bootstrap_is_deterministic(self):
        events = [
            ForecastEvent("e1", "c1", 1, 0.8, 0.6),
            ForecastEvent("e2", "c2", 0, 0.3, 0.5),
            ForecastEvent("e3", "c2", 1, 0.7, 0.6),
        ]
        a = cluster_bootstrap_delta(events, replicates=500, seed=123)
        b = cluster_bootstrap_delta(events, replicates=500, seed=123)
        self.assertEqual(a, b)

    def test_mutation_sensitive_cluster_resampling(self):
        # Two equally sized clusters have opposite paired effects.
        # Correct cluster resampling yields a very wide distribution with endpoints
        # near -1 and +1. Event-level resampling would be much narrower and fail.
        events = []
        for i in range(20):
            events.append(ForecastEvent(f"neg-{i}", "cluster-negative", 1, 1.0, 0.0))  # delta -1
            events.append(ForecastEvent(f"pos-{i}", "cluster-positive", 1, 0.0, 1.0))  # delta +1
        point, lo, hi = cluster_bootstrap_delta(events, replicates=2000, seed=7)
        self.assertAlmostEqual(point, 0.0)
        self.assertLessEqual(lo, -0.9)
        self.assertGreaterEqual(hi, 0.9)


if __name__ == "__main__":
    unittest.main()
