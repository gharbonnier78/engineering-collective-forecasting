# Study 0 - Shadow Engineering Forecasting

Study 0 tests whether collective forecasting can be **measured** in a real engineering setting without becoming a new governance mechanism.

## Primary question

> Can distributed engineering knowledge be transformed into a calibrated and auditable probabilistic signal, and does a prediction-market aggregate add information beyond simple aggregation of independent forecasts?

## Design principle

Only forecast outcomes of activities already planned for operational reasons. Do not create tests, delay releases, alter staffing, or change gate decisions merely to make the experiment easier.

## Population

Eligible participants are adults with legitimate professional knowledge of the forecast topic. Participation is voluntary. The study should deliberately mix relevant perspectives (for example integration, development, test, architecture, environment/operations, functional/product, performance/security when relevant) rather than recruit only one hierarchy level.

A participant must abstain if the outcome is already known to them at forecast time.

## Sequence per contract

1. freeze the Forecast Contract;
2. collect a private independent probability from each participant;
3. freeze those forecasts;
4. open the market phase with virtual points or another approved non-cash mechanism;
5. close before the outcome becomes trivially observable;
6. let the pre-existing engineering process continue unchanged;
7. resolve the event from the predeclared authoritative evidence;
8. score methods and record ambiguity/interference.

## Candidate event families

Use generic categories such as:

- contract/integration test passes before a fixed deadline;
- already-scheduled qualification campaign finds at least one new confirmed critical defect;
- first valid performance run satisfies a predeclared threshold;
- environment reaches a predeclared representativity criterion by a date;
- migration rehearsal completes inside a defined operational window;
- release candidate completes an already-defined pipeline without unplanned manual intervention;
- evidence package is complete against a frozen checklist by the gate date;
- AI/tool pilot satisfies a frozen acceptance criterion on a frozen benchmark.

Do **not** begin with subjective questions such as "Will the release be successful?" or evaluative questions about an employee, team, or supplier.

## Minimal outputs

- event/contract register;
- independent forecast table;
- market close probability and trajectory export;
- resolution record;
- interference record;
- analysis dataset with pseudonymous participant identifiers;
- bounded result report with negative/null results retained.

See `preregistration.md`, `analysis-plan.md`, `organizational-safeguards.md` and `threats-to-validity.md`.
