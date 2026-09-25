import unittest

from analysis.reference_analysis import (
    PairedEvent,
    aggregate_private,
    belief_dispersion,
    brier_score,
    cluster_bootstrap_delta,
    normalized_role_diversity,
)


class ReferenceAnalysisTests(unittest.TestCase):
    def test_brier(self):
        self.assertAlmostEqual(brier_score(0.8, 1), 0.04)
        self.assertAlmostEqual(brier_score(0.2, 0), 0.04)

    def test_private_aggregation(self):
        avg, med = aggregate_private([0.2, 0.5, 0.8])
        self.assertAlmostEqual(avg, 0.5)
        self.assertAlmostEqual(med, 0.5)

    def test_dispersion_zero_when_equal(self):
        self.assertAlmostEqual(belief_dispersion([0.5, 0.5, 0.5]), 0.0)

    def test_role_diversity(self):
        self.assertAlmostEqual(normalized_role_diversity(["dev", "test"], eligible_role_count=2), 1.0)

    def test_cluster_bootstrap_is_deterministic(self):
        events = [
            PairedEvent("e1", "c1", 1, 0.8, 0.6),
            PairedEvent("e2", "c2", 0, 0.3, 0.5),
            PairedEvent("e3", "c2", 1, 0.7, 0.6),
        ]
        a = cluster_bootstrap_delta(events, replicates=500, seed=123)
        b = cluster_bootstrap_delta(events, replicates=500, seed=123)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
