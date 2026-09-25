# Threats to validity

## Construct validity

- **Ambiguous success semantics:** vague questions make the market impossible to score objectively. Mitigation: Forecast Contract with frozen outcome and resolution rule.
- **Market price != truth:** a price reflects the mechanism, participants, incentives and information; it is a forecast signal, not ground truth.
- **Role diversity != information diversity:** category labels are proxies. Mitigation: record locality self-classification and preserve this limitation.

## Internal validity

- **Interference/self-fulfilling effects:** seeing a forecast may change behavior. Mitigation: shadow outputs withheld from operational decision owners; `I=2` exclusion.
- **Outcome knowledge:** insiders may already know the result. Mitigation: explicit abstention.
- **Common-information anchoring:** participants may overweight widely shared information. Mitigation: independent pre-market forecast and exploratory locality analysis.
- **Social/hierarchical pressure:** participants may shade estimates. Mitigation: pseudonymity, voluntary participation, no HR use.
- **Question author leakage:** the question author may encode private expectations in wording. Mitigation: neutral templates and independent contract review.
- **Resolution discretion:** post hoc interpretation can favor a method. Mitigation: predeclared resolver/evidence and void statuses.

## Statistical validity

- **Small J:** Study 0 is a feasibility/estimation study; confidence intervals will be wide.
- **Pseudo-replication:** trades/timestamps are not independent events. Mitigation: contract/cluster as unit.
- **Related contracts:** multiple outcomes can share the same campaign/release. Mitigation: `cluster_id` and cluster bootstrap.
- **Rare outcomes:** few positive or negative events impair calibration/discrimination estimates. Mitigation: report counts and avoid overclaiming.
- **Post-selection:** selecting only interesting contracts after outcomes biases results. Mitigation: prospective register and retained voids.
- **Multiple exploratory analyses:** diversity/role/trajectory findings are exploratory unless separately preregistered.

## External validity

- Corporate prediction-market results from Google, Ford, HP or consumer communities do not automatically transfer to complex engineering qualification.
- One program, country, product family, team structure or platform may not generalize to another.
- A virtual-points mechanism may behave differently from financially incentivized markets.

## Platform validity

- Market-maker parameters influence price dynamics.
- Thin participation can make prices path dependent.
- Hidden platform updates can break reproducibility.
- AI/news assistance can contaminate the intended human-information signal.

Mitigation: freeze/export platform algorithm, version, parameters, visibility, and assistance settings.

## Causal boundary

A conditional market forecast `P(Y | action=A)` is not automatically the interventional causal quantity `P(Y | do(A))`. Study 0 therefore avoids using conditional markets to claim treatment effects or recommend actions.
