# FINAL_BUSINESS_ECONOMIC_MODEL_PLAN

## 0. Scope and Evidence Policy

This document defines the business and economic model to be incorporated into the academic thesis. It is a planning artifact, not evidence of commercial traction.

Every statement must be classified as one of:

- **REAL / VERIFIED**: backed by the product repositories, thesis documentation, executed tests, or professional qualitative validation already documented.
- **BUSINESS ASSUMPTION**: a modeling assumption selected to build economic scenarios.
- **PROJECTED SCENARIO**: a possible future outcome derived from assumptions.
- **MISSING INPUT**: data still required before final financial calculation.

The model must not claim demonstrated clinical error reduction, demonstrated productivity gain, demonstrated sensitivity/specificity improvement, actual sales, actual contracts, or clinical validation.

## 1. Target Market

### Primary User

**Radiologist / diagnostic imaging professional.**

The product is designed as an assistive tool for professionals who review lumbar MRI studies. The user interacts with segmentation overlays, measurements, visual evidence, longitudinal comparison, structured reports, and professional review controls.

Classification: **REAL / VERIFIED**, derived from project scope, professional interviews, product workflow, and validation sessions.

### Buyer

The expected buyer is institutional, not the patient:

- Diagnostic imaging centers.
- Clinics with MRI services.
- Hospitals with lumbar MRI workflows.
- Institutions that need structured review, documentation, and traceability for lumbar MRI studies.

Classification: **BUSINESS ASSUMPTION**, aligned with B2B healthcare software purchasing patterns but not validated by actual sales.

### Indirect Beneficiaries

- Referring medical teams, through clearer structured outputs.
- Patients, indirectly, through a more traceable professional workflow.
- Operational management, through structured review status and documentation.

Classification: **BUSINESS ASSUMPTION**, not evidence of measured benefit.

## 2. Buyer / User Separation

The patient is **not** the primary buyer and should not be treated as the direct customer. The system is not intended for patient self-diagnosis.

| Role | Description | Relationship to Product |
|---|---|---|
| User | Radiologist or imaging professional | Reviews, edits, validates, and exports outputs. |
| Economic buyer | Imaging center, clinic, hospital, or institution | Pays for subscription and integration/support. |
| Technical stakeholder | IT / PACS / infrastructure team | Evaluates deployment, security, integration, and data governance. |
| Indirect beneficiary | Patient and referring care team | Benefits only through professional-mediated workflow. |

## 3. Value Proposition

The value proposition is assistive and workflow-oriented:

> A professional review support tool for lumbar MRI that organizes segmentation, measurements, visual evidence, longitudinal context, and structured reporting in a traceable workflow where the radiologist remains responsible for interpretation and final validation.

Evidence-based value drivers:

- Supports lumbar MRI review with structured visual assistance.
- Provides segmentation overlays and visual evidence.
- Produces geometric measurements derived from masks.
- Allows professional review and correction.
- Supports structured PDF/JSON report generation.
- Supports subjectRef-based history and deterministic demo longitudinal comparison.
- Records corrections and review state for traceability.
- Could contribute to reducing omissions under high workload by highlighting structures or findings for review.
- Could contribute to workflow consistency through structured outputs.

Forbidden claims:

- Demonstrated clinical error reduction.
- Demonstrated productivity increase.
- Demonstrated sensitivity/specificity improvement.
- Autonomous diagnosis.
- Replacement of professional judgment.

Recommended wording:

- "potentially contributes to"
- "is oriented to"
- "seeks to reduce"
- "may support"
- "provides traceability for"

## 4. SaaS Model

Recommended commercial model: **B2B SaaS subscription**.

Core characteristics:

- Monthly subscription per institution or imaging center.
- Included monthly study volume per plan.
- Overage fee per additional study.
- Support and updates included according to tier.
- Optional onboarding/integration fee for enterprise deployments.
- Human review remains mandatory in every tier.

Classification: **BUSINESS ASSUMPTION**.

## 5. Pricing Tiers Draft

Prices are placeholders and must be validated with market research, willingness-to-pay interviews, local healthcare procurement constraints, and measured infrastructure cost.

| Tier | Target Buyer | Included Studies / Month | Users | Features | Support | Overage |
|---|---|---:|---:|---|---|---|
| Starter | Small imaging center or pilot institution | TBD, e.g. 100-250 | TBD, e.g. 2-5 | Upload, segmentation overlays, editable measurements, structured report, basic history | Email / best-effort | TBD per study |
| Professional | Medium diagnostic center or clinic | TBD, e.g. 500-1,500 | TBD, e.g. 5-15 | Starter + review analytics, longitudinal comparison, expanded report workflow, priority updates | Business-hours support | TBD per study |
| Enterprise | Hospital network or high-volume institution | Custom | Custom | Professional + SSO/security review, deployment options, advanced support, integration planning | SLA/custom | Custom |

Pricing alternatives to evaluate:

- Flat monthly subscription.
- Subscription plus overage per study.
- Per-study processing fee with monthly minimum.
- Annual institutional license.
- Pilot fee followed by subscription.

Recommended baseline for financial modeling: subscription plus included volume plus overage.

## 6. Economic Assumptions

The following assumptions are required before building the 36-month cash-flow model.

| Assumption | Type | Source / Justification | Sensitivity |
|---|---|---|---|
| Active clients by month | BUSINESS ASSUMPTION | Must be projected by scenario; no real clients validated. | High |
| New clients per month / quarter | BUSINESS ASSUMPTION | Depends on sales cycle and institutional adoption. | High |
| Churn rate | BUSINESS ASSUMPTION | Needed if recurring SaaS is modeled; no historical churn exists. | Medium/High |
| Studies per client per month | BUSINESS ASSUMPTION | Should be estimated from target institution volume or pilot data. | High |
| Monthly price per tier | BUSINESS ASSUMPTION | Must be validated by willingness-to-pay and competitive analysis. | High |
| Overage price per study | BUSINESS ASSUMPTION | Should cover variable compute/storage/support and margin. | Medium/High |
| Variable cost per study | MISSING INPUT | Requires Cloud Run/AI/DB/storage measurements under real load. | High |
| Fixed cloud baseline | MISSING INPUT | Requires deployed environment measurement. | Medium |
| Support cost per client | BUSINESS ASSUMPTION | Depends on onboarding complexity and issue load. | Medium |
| Maintenance/development cost | BUSINESS ASSUMPTION | Can be modeled as team cost or academic continuation cost. | High |
| Commercial acquisition cost | BUSINESS ASSUMPTION | Requires go-to-market assumption; not measured. | High |
| Inflation / price adjustment | BUSINESS ASSUMPTION | Optional; must specify currency and index if used. | Medium |
| Discount rate | BUSINESS ASSUMPTION | Needed for NPV/VAN; should reflect project risk and local currency context. | High |
| Initial CAPEX / setup | BUSINESS ASSUMPTION | Could include certification, security review, deployment setup, hardware if any. | Medium |

## 7. Cost Structure

### Fixed Costs

Fixed costs should be modeled monthly unless otherwise stated:

- Development and maintenance team.
- Minimal support capacity.
- Administration/accounting/legal.
- Domain, repository, documentation, and project tools.
- Security review and compliance preparation, if applicable.
- Monitoring baseline.
- Commercial/sales baseline.

Cloud fixed baseline is not yet measured and should remain a placeholder until real deployment metrics exist.

### Variable Costs

Variable costs should scale with number of studies, clients, or usage:

- Cloud Run backend/frontend/AI execution.
- AI inference compute.
- Database storage and operations.
- Object storage for studies, overlays, reports, and evidence.
- Network transfer.
- Incremental support.
- Backup/retention overhead.
- LLM/chat provider or self-hosted inference cost, if enabled.

Do not assign exact Cloud cost until measured on the real Cloud environment. Use ranges or placeholders in the first model.

## 8. Scenarios

Recommended horizon: **36 months**.

### Pessimistic Scenario

Purpose: test sustainability under slow adoption and higher cost.

Characteristics:

- Slow client acquisition.
- Low study volume per client.
- Higher churn.
- Lower pricing or discounting.
- Higher variable cost per study.
- Higher support effort per client.
- Delayed enterprise adoption.

Use this scenario to evaluate downside risk and minimum viable operating structure.

### Base Scenario

Purpose: represent a plausible adoption path after pilot validation.

Characteristics:

- Gradual client acquisition.
- Moderate study volume.
- Stable monthly subscription.
- Controlled variable costs.
- Limited support load after onboarding.
- Some overage revenue.

Use this scenario as the central case once assumptions are validated.

### Optimistic Scenario

Purpose: test upside if adoption and retention are favorable.

Characteristics:

- Faster client acquisition.
- Higher study volume.
- Higher tier mix, including Professional/Enterprise.
- Lower churn.
- Better infrastructure efficiency per study.
- Higher overage revenue.
- Stronger referral/network effect.

Use this scenario to evaluate scalability and investment attractiveness.

## 9. Cash-Flow Structure

Monthly cash-flow table structure:

| Month | Active Clients | New Clients | Churned Clients | Subscription Revenue | Overage Revenue | Total Revenue | Variable Costs | Fixed Costs | Initial CAPEX / One-off Costs | Operating Cash Flow | Net Cash Flow | Accumulated Cash Flow |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 36 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Formulas:

- Active Clients(t) = Active Clients(t-1) + New Clients(t) - Churned Clients(t)
- Subscription Revenue = sum(active clients by tier × monthly tier price)
- Overage Revenue = max(0, actual studies - included studies) × overage price
- Total Revenue = Subscription Revenue + Overage Revenue
- Variable Costs = processed studies × variable cost per study + variable support costs
- Operating Cash Flow = Total Revenue - Variable Costs - Fixed Costs
- Net Cash Flow = Operating Cash Flow - CAPEX / one-off costs
- Accumulated Cash Flow = previous accumulated cash flow + Net Cash Flow

## 10. Break-Even Methodology

Break-even can be calculated in two complementary ways:

### Monthly Operating Break-Even

The first month in which:

```text
Total Revenue >= Fixed Costs + Variable Costs
```

### Accumulated Break-Even

The first month in which:

```text
Accumulated Cash Flow >= 0
```

Required inputs:

- Price by tier.
- Active clients by month.
- Study volume by client/tier.
- Variable cost per study.
- Fixed monthly cost.
- Initial CAPEX / one-off costs.

## 11. Payback Methodology

Payback is the first month when accumulated cash flow recovers the initial investment:

```text
Payback Month = first month where Accumulated Cash Flow >= 0
```

If accumulated cash flow remains negative through month 36, payback is not reached within the modeled horizon.

## 12. VAN / NPV Methodology

VAN (Valor Actual Neto) is calculated by discounting monthly net cash flows:

```text
VAN = -Initial Investment + sum(Net Cash Flow_t / (1 + monthly_discount_rate)^t)
```

Where:

```text
monthly_discount_rate = (1 + annual_discount_rate)^(1/12) - 1
```

The discount rate must be explicitly justified. For this project, candidate approaches are:

- Conservative academic startup risk rate.
- Local currency opportunity cost.
- Institution-specific required return.
- Scenario-specific sensitivity range.

No VAN should be finalized until price, cost, client growth, and discount rate assumptions are defined.

## 13. TIR / IRR Methodology

TIR is the discount rate that makes VAN equal to zero:

```text
0 = -Initial Investment + sum(Net Cash Flow_t / (1 + TIR_monthly)^t)
```

Report both:

- Monthly TIR.
- Annualized TIR:

```text
TIR_annual = (1 + TIR_monthly)^12 - 1
```

TIR should not be calculated until the cash-flow series is complete and includes initial investment.

## 14. Missing Real Inputs

The economic model still requires:

- Measured Cloud Run cost under representative study volume.
- AI inference latency and compute cost per study.
- Storage per study, per overlay, and per report.
- Database growth and backup cost.
- Support time per institution.
- Expected monthly study volume per target center.
- Willingness-to-pay interviews with buyers, not only users.
- Competitive pricing benchmark.
- Sales cycle length for clinics/hospitals.
- Churn/retention assumptions.
- Legal, regulatory, and compliance cost assumptions.
- Currency and inflation policy for the model.
- Discount rate.

## 15. Data Still Requiring Validation

Before final thesis financial tables:

- Validate buyer persona with at least one institution decision-maker or administrator.
- Validate tier definitions with professionals and operational stakeholders.
- Run Cloud cost measurement on deployed DEV/DEMO-like environment.
- Estimate real study volume from public reports, institutional input, or pilot data.
- Compare pricing with similar imaging AI / workflow SaaS tools where data is available.
- Decide whether model is ARS, USD, or dual-currency.
- Decide whether salaries are modeled as opportunity cost, real startup cost, or excluded academic cost.
- Define whether regulatory certification is outside scope or included as future CAPEX.

## 16. Recommended Next Steps

1. Add a thesis chapter or section titled **Modelo de negocio y viabilidad economica** after technical results or before planning/conclusions.
2. Keep it separate from technical evaluation results.
3. Convert this plan into LaTeX tables:
   - target market and stakeholder table;
   - value proposition table;
   - pricing tier table;
   - assumption table;
   - cost structure table;
   - scenario definition table;
   - financial metric methodology table.
4. Build a spreadsheet model with 36 monthly rows and three scenario tabs.
5. Add sensitivity tables for price, client count, variable cost per study, and discount rate.
6. Only calculate break-even, Payback, VAN, and TIR after assumptions are approved.
7. Mark every final value as assumption-based projection, not real commercial performance.

## 17. Proposed LaTeX Location

Recommended structure:

- New chapter: **Modelo de negocio y viabilidad economica**.
- Place after `chapters/capitulo_13_resultados_evaluacion.tex` and before `chapters/capitulo_14_planificacion_academica.tex`, or renumber planning accordingly.
- Alternative: add as a major section inside planning, but this is less clean because business model and academic roadmap answer different questions.

Recommended sections:

1. Mercado objetivo y actores.
2. Propuesta de valor.
3. Modelo comercial B2B SaaS.
4. Supuestos economicos.
5. Estructura de costos.
6. Escenarios proyectados.
7. Flujo de fondos e indicadores.
8. Limitaciones del modelo economico.

## 18. Readiness for Excel

Ready to build Excel / spreadsheet model: **PARTIAL**.

The structure is ready, but final calculations should wait for validated assumptions. A spreadsheet can be created now with placeholder inputs and formulas, as long as outputs remain clearly labeled as scenario projections.