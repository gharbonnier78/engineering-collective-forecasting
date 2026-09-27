"""Toy check: extremizing around a shared prior estimated from meta-predictions.

ADEMP and success criteria frozen in ademp-pivot.md
(sha256 cf7a1164aaf6d8c203167b52df7177923be24ba9675d1a543761a6abdfb20412) before first execution.

Same data-generating mechanism as sim_delta.py, plus one meta-prediction per forecaster:
"what average probability will your colleagues give?"
"""
import numpy as np
from numpy.polynomial.hermite_e import hermegauss

SEED = 20260926
PI, N, SIGMA_R, SIGMA_M, A = 0.65, 6, 0.3, 0.3, 2.0
L0 = float(np.log(PI / (1 - PI)))
SCEN = {"S1 info privée dominante": (0.5, 0.25), "S2 info commune dominante": (0.2, 0.6)}
PRIMARY = dict(a=2.0, lam=0.3, scale="prob")
_Z, _W = hermegauss(60)
_W = _W / _W.sum()                      # E[f(Z)], Z ~ N(0, 1)

sig = lambda x: 1.0 / (1.0 + np.exp(-x))
logit = lambda p: np.log(p / (1.0 - p))


def other_prob_given_y(base, mu, sigma_r):
    """E[p_j | y=1, shared] and E[p_j | y=0, shared] for a colleague j, per contract (Gauss-Hermite).

    Given y (s = +/-1), logit p_j = base + 2*mu*x_j + eps_j ~ N(base + 2*mu^2*s, (2*mu)^2 + sigma_r^2).
    """
    sd = np.sqrt((2 * mu) ** 2 + sigma_r ** 2)
    return [(sig((base + 2 * mu * mu * s)[:, None] + sd * _Z[None, :]) * _W).sum(1) for s in (1.0, -1.0)]


def draw(g, J, mu_priv, mu_pub, sigma_r=SIGMA_R, sigma_m=SIGMA_M):
    y = g.random(J) < PI
    s = np.where(y, 1.0, -1.0)
    pub = 2 * mu_pub * g.normal(s * mu_pub, 1.0)                     # shared log-likelihood ratio
    x = g.normal(s[:, None] * mu_priv, 1.0, size=(J, N))             # private signals
    base = L0 + pub
    L_true = base[:, None] + 2 * mu_priv * x                          # each forecaster's Bayesian posterior
    L_rep = L_true + g.normal(0, sigma_r, (J, N))                     # reported own forecast (logit)
    p_true = sig(L_true)
    A1, A0 = other_prob_given_y(base, mu_priv, sigma_r)
    meta_prob = p_true * A1[:, None] + (1 - p_true) * A0[:, None]     # E[p_j | info_i]
    meta_logit = base[:, None] + 2 * mu_priv ** 2 * (2 * p_true - 1)  # E[logit p_j | info_i]
    return dict(J=J, y=y.astype(float), base=base, L_rep=L_rep, L_true=L_true, meta_prob=meta_prob,
                meta_logit=meta_logit, eta=g.normal(0, sigma_m, (J, N)),
                mkt_core=base + 2 * mu_priv * x.sum(1))


def meta_extremized(d, a, lam, scale):
    """logit p = Mbar + a (Lbar - Mbar): extremize away from the prior estimated by meta-predictions."""
    M = logit(np.clip(d["meta_prob"], 1e-12, 1 - 1e-12)) if scale == "prob" else d["meta_logit"]
    M_rep = (1 - lam) * M + lam * d["L_rep"] + d["eta"]               # false consensus + report noise
    Lbar, Mbar = d["L_rep"].mean(1), M_rep.mean(1)
    return sig(Mbar + a * (Lbar - Mbar))


def scores(d, g, tau, cfg=PRIMARY):
    Y, L = d["y"], d["L_rep"]
    bs = lambda p: (p - Y) ** 2
    Lbar = L.mean(1)
    return {
        "individuel": ((sig(L) - Y[:, None]) ** 2).mean(1),
        "moyenne": bs(sig(L).mean(1)),
        "ext@0.5": bs(sig(A * Lbar)),
        "ext@base": bs(sig(L0 + A * (Lbar - L0))),
        "ext@méta": bs(meta_extremized(d, **cfg)),
        "marché": bs(sig(d["mkt_core"] + g.normal(0, tau, d["J"]))),
    }


def sanity_checks():
    g = np.random.default_rng(1)
    mu = 0.5
    d = draw(g, 50, mu, 0.25)
    for j in range(5):                                   # 1) quadrature and closed form vs Monte Carlo
        b, pt, n = d["base"][j], sig(d["L_true"][j, 0]), 400_000
        xj = g.normal(np.where(g.random(n) < pt, mu, -mu), 1.0)
        mc_p = sig(b + 2 * mu * xj + g.normal(0, SIGMA_R, n)).mean()
        mc_l = (b + 2 * mu * xj).mean()
        assert abs(mc_p - d["meta_prob"][j, 0]) < 3e-3, (mc_p, d["meta_prob"][j, 0])
        assert abs(mc_l - d["meta_logit"][j, 0]) < 1e-2, (mc_l, d["meta_logit"][j, 0])
    d = draw(g, 1000, 0.0, 0.6, sigma_r=0.0, sigma_m=0.0)  # 2) no private info, no noise -> = mean
    for scale in ("prob", "logit"):
        assert np.allclose(meta_extremized(d, 2.0, 0.0, scale), sig(d["L_rep"]).mean(1), atol=1e-9)
    d = draw(g, 20_000, 0.5, 0.0)                           # 3) no public info -> meta less extreme
    own = np.mean(np.abs(d["L_true"] - L0))
    assert np.mean(np.abs(d["meta_logit"] - L0)) < own
    assert np.mean(np.abs(logit(d["meta_prob"]) - L0)) < own


def main():
    sanity_checks()
    print("contrôles de code : OK (quadrature = Monte-Carlo ; sans info privée ni bruit, ext@méta = moyenne ;"
          " sans info publique, méta moins extrême)\n")
    g = np.random.default_rng(SEED)
    Jb = 200_000
    draws, res = {}, {}
    print(f"climatologie BS = {PI * (1 - PI):.4f} | configuration primaire : a=2, λ=0,3, méta en probabilité, σ_m=0,3\n")
    for name, (mp, mq) in SCEN.items():
        d = draw(g, Jb, mp, mq)
        draws[name] = d
        s0, s1 = scores(d, g, 0.0), scores(d, g, 0.75)
        m = {k: float(v.mean()) for k, v in s0.items()}
        m["marché mince"] = float(s1["marché"].mean())
        gap = m["moyenne"] - m["marché"]
        diff = s0["ext@méta"] - s0["moyenne"]
        half = 1.96 * diff.std(ddof=1) / np.sqrt(Jb)
        res[name] = dict(m=m, gap=gap, ci=(diff.mean() - half, diff.mean() + half))
        print(name)
        print("  BS : " + " | ".join(f"{k} {v:.4f}" for k, v in m.items()))
        print("  part de l'écart moyenne→marché idéal comblée : "
              + " | ".join(f"{k} {(m['moyenne'] - m[k]) / gap:+.0%}" for k in ("ext@0.5", "ext@base", "ext@méta")))
        print(f"  ext@méta − moyenne = {diff.mean():+.4f}  IC95 [{diff.mean() - half:+.4f} ; {diff.mean() + half:+.4f}]")
        for tau, sc in ((0.0, s0), (0.75, s1)):
            dd = sc["marché"] - sc["ext@méta"]
            print(f"  Δ marché(τ={tau}) − ext@méta : E={dd.mean():+.4f}  sd={dd.std():.4f}"
                  f"  J(80 %)≈{(2.8016 * dd.std() / abs(dd.mean())) ** 2:,.0f}")
        print()

    S1, S2 = (res[k] for k in SCEN)
    share = lambda r, k: (r["m"]["moyenne"] - r["m"][k]) / r["gap"]
    C1 = S2["ci"][1] <= 0.001
    C2 = share(S1, "ext@méta") >= share(S1, "ext@base")
    print(f"C1 (S2, pas de dégradation) : {'PASSE' if C1 else 'ÉCHOUE'} — borne haute {S2['ci'][1]:+.4f} (seuil +0,001)")
    print(f"C2 (S1, gain ≥ ext@base)   : {'PASSE' if C2 else 'ÉCHOUE'} — {share(S1, 'ext@méta'):.0%} vs {share(S1, 'ext@base'):.0%}")

    print("\nSensibilité (mêmes tirages)   a  λ    échelle | S1 part comblée | S2 ext@méta − moyenne [borne haute] | C1")
    n_ok = n_req = 0
    for a in (2.0, 3.0):
        for lam in (0.0, 0.3, 0.6):
            for scale in ("prob", "logit"):
                bs = []
                for name in SCEN:
                    d = draws[name]
                    Y = d["y"]
                    bs.append((((meta_extremized(d, a, lam, scale) - Y) ** 2), (sig(d["L_rep"]).mean(1) - Y) ** 2))
                (b1x, b1m), (b2x, b2m) = bs
                sh = (b1m.mean() - b1x.mean()) / S1["gap"]
                dd = b2x - b2m
                hi = dd.mean() + 1.96 * dd.std(ddof=1) / np.sqrt(len(dd))
                ok = hi <= 0.001
                if lam <= 0.3:
                    n_req += 1
                    n_ok += int(ok)
                print(f"                              {a:.0f}  {lam:.1f}  {scale:<5}  | {sh:+5.0%}           | {dd.mean():+.4f} [{hi:+.4f}]"
                      f"                    | {'ok' if ok else 'ÉCHEC'}")
    robust = C1 and n_ok == n_req
    if robust and C2:
        verdict = "RECOMMANDER (C1 et C2 passent ; C1 robuste pour λ ≤ 0,3)"
    elif robust:
        verdict = "RECOMMANDER comme agrégat prudent (C1 robuste, C2 échoue)"
    else:
        verdict = "EXPLORATOIRE seulement (C1 échoue ou n'est pas robuste)"
    print(f"\nC1 pour λ ≤ 0,3 : {n_ok}/{n_req} configurations\nDécision (règle figée) : {verdict}")


if __name__ == "__main__":
    main()
