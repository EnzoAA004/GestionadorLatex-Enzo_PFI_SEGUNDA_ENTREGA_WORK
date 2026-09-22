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
