# Independent publication-readiness reviewer prompt

## Role

Review this pull request as an **external protocol-publication and provenance review against an already accepted scientific baseline**.

Do not edit, merge, rebase or push to the branch.

## Canonical objects

- Repository: https://github.com/gharbonnier78/engineering-collective-forecasting
- Pull request: https://github.com/gharbonnier78/engineering-collective-forecasting/pull/2
- Accepted scientific baseline: https://github.com/gharbonnier78/engineering-collective-forecasting/commit/b38feb509f9b3ed94e37f590b441e0e906601341
- Pinned harness: https://github.com/gharbonnier78/scientific-research-harness/blob/e8e043c2b66a74ccacd023d67a32f989885449eb/HARNESS.md
- Publication-prep Chronicle: research/chronicle/2026-09-27--protocol-publication-prep.md
- Paper: paper/engineering_collective_forecasting.tex
- Related work: paper/sections/01b-related-work.tex
- Operating characteristics: paper/sections/02b-design-operating-characteristics.tex
- Design simulation provenance: analysis/design_simulation/README.md
- Publication plan: docs/publication-plan.md

Use the exact current PR head shown by GitHub when performing the review, and report that SHA in the review.

## Review boundary

The accepted Study 0A/0B scientific design is not being reopened unless this PR accidentally changes it.

Verify that publication-oriented changes do not silently alter:

- Study 0A admission or continuation logic;
- Study 0B scientific unit or target population;
- crowd-vs-owner primary contrast;
- base-rate subset logic;
- private/pre-resolution visibility safeguards;
- actor/observer composition;
- fixed aggregation rule;
- cluster-level uncertainty analysis;
- G2 organizational authorization boundary.

## Publication-readiness checks

### A. External-facing manuscript

1. Does the abstract read as a protocol paper rather than an internal review log?
2. Are protocol contributions explicit but bounded?
3. Is internal PR/gate history absent from the scholarly narrative?
4. Is terminology understandable without prior repository context?
5. Is Figure 1 readable without broken/hyphenated box text?

### B. Related work and source fidelity

6. Are claims about prediction markets, direct polling, meta-predictions, extremization, software expert estimation and measurement reactivity supported by the cited sources?
7. Are transfer boundaries explicit, especially for behavioral question-effect studies and software-effort estimation?
8. Is the project aggregator clearly distinguished from Bayesian Truth Serum, Surprisingly Popular and other published algorithms?
9. Are relevant source notes present and consistent with the manuscript?

### C. Design operating characteristics

10. Does the manuscript table match the preserved reference output?
11. Do sim_pivot.py and sim_continuation.py retain the SHA-256 values recorded in analysis/design_simulation/README.md?
12. Is the J≈30 / delta_NI=0.02 interpretation correctly limited to a screening/non-inferiority continuation rule rather than superiority power?
13. Are the toy-model assumptions and optimistic independence limitation visible?

### D. Author, AI and publication boundary

14. Is Independent Researcher a clear affiliation without implying employer endorsement?
15. Is the AI-assistance disclosure explicit about drafting/code/review use and human responsibility?
16. Is manuscript-preparation AI use distinguished from participant AI-assistance metadata?
17. Does the paper preserve the requirement for explicit organizational authorization before external publication of employer-derived results?

### E. Reproducibility

18. Do research-assurance and paper workflows pass on the exact PR head?
19. Does the exact-head PDF rebuild deterministically and remain visually readable?
20. Are source, code, simulation seeds, provenance and replay commands recoverable?

## Required disposition

Return exactly one:

- ACCEPT
- PARTIAL ACCEPT
- REJECT

Then provide:

1. exact head SHA reviewed;
2. any blocking publication-readiness findings;
3. non-blocking editorial suggestions;
4. confirmation whether the accepted scientific baseline was preserved;
5. exact next admissible action.

Do not request a redesign merely because a different scientific study could also be interesting.
