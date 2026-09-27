# Publication plan — protocol stage

Status: **publication preparation; no Study 0 outcome data exist**

Last checked: **2026-09-27**

The accepted Study 0A/0B design is an appropriate object for a first **protocol publication**, not a results paper.

## 1. Citable protocol release

After this publication-preparation PR is independently reviewed:

1. create an immutable GitHub release/tag;
2. archive that release through the Zenodo GitHub integration to obtain a permanent DOI;
3. cite the immutable release/DOI from subsequent Study 0A and Study 0B artifacts.

Zenodo documents that enabled GitHub repositories can have new releases automatically ingested and archived:
https://help.zenodo.org/docs/github/

## 2. Prospective registration

Before Study 0B data collection, create a time-stamped registration/preregistration of the deployment-specific protocol after Study 0A has established the feasible event families and before Study 0B outcomes are inspected.

OSF registrations create a frozen/read-only record of the study plan and public registrations can receive a DOI:
https://help.osf.io/article/330-welcome-to-registrations

The repository preregistration remains the machine-readable/source-controlled authority; an OSF registration would provide an external immutable registration surface.

## 3. Preprint route

A preprint can be considered after the external-facing protocol manuscript is stable.

Current arXiv operational points to re-check immediately before submission:

- first submission to arXiv or to a new category can require endorsement under the current endorsement system:
  https://info.arxiv.org/help/endorsement.html
- arXiv's Computer Science category has a specific moderation practice for review articles and position papers; if the manuscript could be classified that way, verify current eligibility rather than assuming a CS upload will be accepted:
  https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/

Because this manuscript is a methods/protocol contribution rather than a literature review, category fit should be decided from the final manuscript and current arXiv moderation guidance. Statistical-method categories may be relevant, but no category is hard-coded here.

## 4. Registered Report route

The stronger peer-reviewed path is a Registered Report after Study 0A, when the observed contract-funnel yield, clean-resolution rate, event-family mix and projected Study 0B throughput are known but before Study 0B outcome-bearing forecasting results exist.

EMSE describes the software-engineering Registered Report process as:

- Stage 1: methods and planned analyses are reviewed before the study is executed;
- after in-principle acceptance, the study is run according to the approved protocol;
- Stage 2: the results paper is submitted to Empirical Software Engineering, including null/negative outcomes if the approved protocol was followed.

Current overview:
https://emsejournal.github.io/registered_reports/

Conference partners and calls vary by year. ESEM, MSR and ICSME have all hosted Stage-1 Registered Report tracks; the live call must be checked when Study 0A is complete.

## 5. Organizational publication authorization

The protocol's G2 gate requires explicit organizational authorization before:

- live employee-data collection;
- external publication of results derived from employer projects, systems or internal evidence, even if those results are aggregated or anonymized.

No internal program, customer, supplier, employee or proprietary evidence should be placed in a public release merely because it has been de-identified.

## 6. Publication package

A protocol release should contain:

- the LaTeX source and deterministic PDF;
- CITATION.cff;
- the frozen Study 0A/0B protocol and schemas;
- public synthetic templates;
- reference analysis code and tests;
- design-simulation scripts plus frozen seeds/reference outputs;
- source/provenance notes;
- a clear author/AI-assistance declaration;
- the exact immutable repository reference used to build the manuscript.

The later results package should be separately authorized and should not retroactively modify the frozen protocol record.
