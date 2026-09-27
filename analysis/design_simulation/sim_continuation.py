"""Operating characteristics of the Study 0B continuation rule (PR #1 @ a936054, preregistration §7).

Plan (frozen in this docstring; file hashed before first execution):
A  Probability that the rule "upper 95 % cluster-bootstrap bound of mean Delta_owner <= delta_NI"
   is met at the recommended minimum scale, for several true crowd-vs-owner situations.
D  Toy model of sim_pivot.py: y ~ Bernoulli(0.65); one public signal; 6 private-signal forecasters
   (report noise 0.3 logit); S1 mostly private information, S2 mostly shared.
   Owner types: "actor" (1 private signal, +0.4 logit optimism), "unbiased" (1 private signal),
   "well-informed" (4 private signals). Contracts independent (no intra-cluster correlation: optimistic).
E  E[Delta_owner] = E[BS(crowd) - BS(owner)]; P(continue) = P(upper bound <= delta_NI).
M  Crowd = preregistered primary aggregator (meta recalibration, a = 2) with Bayesian meta-predictions,
   30 % projection and 0.3 logit meta noise. J = 32 contracts in K = 8 or 16 equal clusters;
   2,000 simulated studies x 2,000 bootstrap draws; delta_NI in {0.02, 0.05, 0.08}.
P  Table of E[Delta_owner] and P(continue).
"""
import numpy as np
from sim_pivot import draw, meta_extremized, sig, L0, SIGMA_R

SEED = 20260927
g = np.random.default_rng(SEED)
SCEN = {"S1 privée": (0.5, 0.25), "S2 commune": (0.2, 0.6)}
OWNERS = {"acteur optimiste": (1, 0.4), "sans biais": (1, 0.0), "bien informé": (4, 0.0)}
DELTAS, J = (0.02, 0.05, 0.08), 32


def delta_owner(d, mu_priv, k_signals, bias):
    s = np.where(d["y"] > 0.5, 1.0, -1.0)
    x_owner = g.normal(s[:, None] * mu_priv, 1.0, size=(d["J"], k_signals))
    L_owner = d["base"] + 2 * mu_priv * x_owner.sum(1) + bias + g.normal(0, SIGMA_R, d["J"])
    p_crowd = meta_extremized(d, a=2.0, lam=0.3, scale="prob")
    return (p_crowd - d["y"]) ** 2 - (sig(L_owner) - d["y"]) ** 2


print(f"J = {J} contrats ; règle : borne haute IC95 (bootstrap par cluster) de mean Δ_owner ≤ δ_NI\n")
print(f"{'scénario':<11} {'propriétaire':<17} {'E[Δ_owner]':>10} | " + " | ".join(f"K={K}: " + " ".join(f"δ={x:.2f}" for x in DELTAS) for K in (8, 16)))
for sname, (mp, mq) in SCEN.items():
    for oname, (k, bias) in OWNERS.items():
        big = draw(g, 200_000, mp, mq)
        true_mean = delta_owner(big, mp, k, bias).mean()
        cells = []
        for K in (8, 16):
            probs = np.zeros(len(DELTAS))
            R = 2000
            for _ in range(R):
                d = draw(g, J, mp, mq)
                dl = delta_owner(d, mp, k, bias)
                cm = dl.reshape(K, J // K).mean(1)                       # equal-size cluster means
                boot = cm[g.integers(0, K, size=(2000, K))].mean(1)
                hi = np.quantile(boot, 0.975)
                probs += np.array([hi <= x for x in DELTAS])
            cells.append(" ".join(f"{p / R:7.0%}" for p in probs))
        print(f"{sname:<11} {oname:<17} {true_mean:>+10.3f} | " + " | ".join(f"      {c}" for c in cells))
