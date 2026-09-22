# Financial model assumptions - pending validation

This document accompanies `financial/PFI_RM_LUMBAR_FINANCIAL_MODEL_36M.xlsx`.

The model is an academic, editable 36-month financial model in USD. It does not represent audited financial projections, confirmed sales, confirmed reimbursement, or productive operating evidence. All assumptions are intentionally visible and editable in the workbook.

## Missing validations

1. Willingness-to-pay interviews with imaging centers, hospitals, teaching institutions, and potential administrative buyers.
2. Real pilot funnel: number of reachable institutions, conversion rates, sales-cycle duration, procurement blockers, and expected ramp.
3. True monthly processed-study volume per customer tier using anonymized operational evidence.
4. Retention and churn evidence after supervised pilot usage.
5. Cloud billing benchmark for ingestion, preprocessing, AI inference, storage, observability, and download/export workflows.
6. Support workload per institution, including onboarding, technical support, and professional review coordination.
7. Regulatory, legal, data-governance, and privacy costs for any production or clinical-adjacent deployment.
8. Reimbursement, institutional budget availability, and buyer responsibility for the proposed service.
9. Maintenance staffing, model monitoring, incident response, and security hardening cost.
10. Tax, inflation, foreign-exchange, financing, and local accounting treatment.

## Pricing note

The workbook uses three provisional tiers: Starter, Professional, and Enterprise. Prices and included volumes are placeholders for thesis-level scenario modeling and must be replaced with validated commercial data before any real investment or deployment decision.

## Scenario note

Pesimista, Base, and Optimista differ in pricing, customer acquisition, churn, usage, variable cost efficiency, fixed cost structure, and upfront investment. The active scenario selector is in `01_ASSUMPTIONS!B2`.

## Formula note

The workbook includes formula-driven monthly cash flow, operating break-even, payback, VAN/NPV, TIR/IRR, and sensitivity outputs. Scenario summary and sensitivity tables are generated from the same assumption mechanics and documented as academic planning evidence.

## Sanity checks and model interpretation

A formula-level sanity audit was performed after creating the 36-month workbook. The audit recomputed customer growth, study volume, subscription revenue, overage revenue, variable costs, fixed costs, initial investment, net cash flow, discounted cash flow, VAN/NPV, TIR/IRR, operating break-even, payback, and sensitivity outputs independently from the workbook assumptions.

The scenario ordering is internally consistent under the current assumptions. The Base scenario has a worse VAN than the Pesimista scenario because it scales activity without reaching operating break-even inside the 36-month horizon. Compared with Pesimista, Base generates materially higher revenue, but it also carries higher fixed costs, higher variable costs, higher marketing expense, and higher initial investment. Over 36 months, Base improves gross activity but still produces negative operating results in every month; the extra contribution does not compensate for the larger fixed-cost and investment base. Base also uses a lower annual discount rate than Pesimista, so its later negative cash flows are discounted less heavily.

The independent audit classified this behavior as `EXPECTED_BY_ASSUMPTIONS`, not as a model formula error. The result should not be interpreted as evidence that the Base business case is intrinsically worse in the real world. It means the current provisional Base assumptions combine moderate pricing, moderate adoption, substantial fixed operating cost, and insufficient contribution margin within the 36-month window.

Key audit observations:

1. Customer formulas follow `customers_t = customers_t-1 + acquisitions - churn`, with churn applied to the prior active customer base and acquisitions added once per tier.
2. Customer counts remain non-negative, tier totals reconcile to total customers, and tier mix sums to 100% in the audited months.
3. Revenue formulas apply monthly fee times active customers, then calculate overage only on studies above each tier's included allowance.
4. Study volume is calculated as active customers times studies per customer per month.
5. Variable study costs are applied once to total studies and are not applied again to overage.
6. Fixed costs and initial investment are not duplicated; initial investment is applied only in month 1.
7. VAN uses monthly discounting derived from `(1 + annual_rate)^(1/12) - 1` and includes the month-1 investment through the month-1 net cash flow.
8. TIR is only reported when the cash-flow sign pattern supports a valid IRR. Pesimista and Base remain negative over the audited horizon, so `n.a.` is appropriate.
9. Operating break-even and payback are intentionally different metrics: break-even is the first month with operating result >= 0, while payback is the first month with cumulative cash flow >= 0.
10. A temporary 48/60-month projection did not show Base reaching operating break-even or payback under the current assumptions.

The workbook should therefore remain unchanged unless future evidence changes the underlying assumptions or a later audit identifies an actual formula/modeling defect.

## Cloud cost methodology refinement

This refinement replaces the initial cloud-cost placeholders with technically defendible estimates while keeping pricing, acquisition, churn, and institutional study volume marked as business assumptions. No Cloud resource was created, modified, or deployed for this update.

Evidence used:

- Current deployed state: Artifact Registry/WIF, Backend Cloud Run DEV, and Frontend Cloud Run DEV are deployed/validated.
- Not deployed: private AI Cloud Run, Cloud SQL, Secret Manager, productive Storage, DEMO environment, and live monitoring/alerting.
- Local performance baseline: Frontend p95 CPU ~1.98% / RAM ~14.68 MiB; Backend p95 CPU ~7.67% / RAM ~267.50 MiB; AI p95 CPU ~346.62% / RAM ~801.20 MiB / peak RAM ~940.80 MiB; Postgres p95 CPU ~4.13% / RAM ~37.19 MiB.
- Planned DEV resources: Backend Cloud Run 1 vCPU/512Mi/min 0/max 2/concurrency 80/timeout 300s; Frontend Cloud Run 1 vCPU/256Mi/min 0/max 2/concurrency 80; planned AI Cloud Run 2 vCPU/2Gi/min 0/max 1/concurrency 4; planned Cloud SQL PostgreSQL 15 Enterprise db-f1-micro, us-central1, ZONAL, 10 GB, no HA/backups/PITR for DEV.

Refined workbook inputs:

| Input | Pesimista | Base | Optimista | Status |
|---|---:|---:|---:|---|
| Cloud cost per study | 0.20 | 0.08 | 0.03 | ESTIMATED |
| Storage cost per study | 0.06 | 0.03 | 0.015 | ESTIMATED |
| AI processing cost per study | 0.30 | 0.10 | 0.04 | ESTIMATED |
| Fixed infrastructure/month | 45 | 65 | 110 | ESTIMATED |

These values are not billing measurements. They are a planning envelope derived from request-based Cloud Run economics, scale-to-zero assumptions, projected Cloud SQL fixed cost, light storage retention, and the local resource baseline. The AI duration per study remains a missing input; therefore, AI processing is kept as an estimated range rather than a verified cost.

Refined Base result:

- VAN/NPV: -31692 USD
- Operating break-even: month 17
- Payback: >36 months
- Annualized TIR: -5.19%

The previous Base-negative interpretation was correct for the prior placeholder inputs. After replacing the technical cloud placeholders, Base reaches operating break-even inside the 36-month horizon, but it still does not reach payback or a positive VAN. This must be read narrowly: technical cloud cost was refined; market pricing and commercial adoption remain unvalidated.

## Base Viable Exploratory

The workbook now includes `08_BASE_VIABLE` as a sensitivity-only sheet. It does not replace Pesimista, Base, or Optimista and must not be described as a forecast. It shows the minimum explored direction in which the refined Base economics remain viable:

- Acquisition multiplier: 1.00x
- Pricing multiplier: 1.00x
- Fixed operating cost multiplier: 0.95x
- VAN/NPV: -21162 USD
- Payback: month 36

Remaining missing inputs are institutional willingness-to-pay, real monthly study volumes per customer tier, real inference duration per complete study on Cloud Run, real Cloud billing after deployment, retention/storage policy, support burden, and observed acquisition/churn.
