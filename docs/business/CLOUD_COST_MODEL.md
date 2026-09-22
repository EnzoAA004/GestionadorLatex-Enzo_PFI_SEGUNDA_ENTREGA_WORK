# Cloud cost model

This document refines the economic model's technical cloud assumptions. It is a planning estimate, not billing evidence, and no Google Cloud resources were created or modified for this refinement.

## Deployed resources

| Resource | Status | Evidence |
|---|---|---|
| Artifact Registry / WIF | DEPLOYED + VALIDATED | Backend cloud roadmap: WIF live, first Backend + Frontend image publish succeeded. |
| Backend Cloud Run DEV | DEPLOYED + VALIDATED | `pfi-backend-dev`, Ready, smoke-tested. |
| Frontend Cloud Run DEV | DEPLOYED + VALIDATED | `pfi-frontend-dev`, Ready, browser login/CORS smoke-tested. |

## Planned / not deployed resources

| Resource | Status | Planned configuration |
|---|---|---|
| AI Cloud Run private | NOT DEPLOYED | Planned module: 2 vCPU, 2Gi, min 0, max 1, concurrency 4, internal only. |
| Cloud SQL | NOT DEPLOYED | PostgreSQL 15, Enterprise, db-f1-micro, us-central1, ZONAL, 10GB, no HA/backups/PITR for DEV, deletion protection true. |
| Secret Manager | NOT DEPLOYED | Two DEV secret containers planned, no values in Terraform. |
| Product Storage | NOT DEPLOYED | Architecture target for assets/model artifacts; no productive bucket workflow validated. |
| DEMO environment | NOT DEPLOYED | Plan-only; no workflow run for real. |
| Monitoring/alerting live | NOT DEPLOYED | Designed, not created. |

## Billing drivers

| Component | Status | Resource | Billing driver | Estimated monthly cost | Estimated cost/study | Confidence | Source / assumption |
|---|---|---|---|---:|---:|---|---|
| Frontend Cloud Run | DEPLOYED_DEV | 1 vCPU / 256Mi / min 0 / max 2 | request CPU+memory seconds | 0-2 | <0.01 | MEDIUM | Terraform DEV + Cloud Run official pricing |
| Backend Cloud Run | DEPLOYED_DEV | 1 vCPU / 512Mi / min 0 / max 2 | request CPU+memory seconds | 0-5 | <0.02 | MEDIUM | Terraform DEV + local p95 baseline |
| AI compute | NOT_DEPLOYED_ESTIMATE | planned 2 vCPU / 2Gi / min 0 / max 1 | active inference seconds | usage-dependent | 0.04-0.30 | LOW | local CPU/RAM baseline; duration missing |
| Cloud SQL | NOT_DEPLOYED_PROJECTED | db-f1-micro + 10GB SSD | always-on instance + disk | 9-12 | volume-dependent | MEDIUM | Backend CLOUD-05 plan + official Cloud SQL pricing |
| Storage | PLANNED_ESTIMATE | Standard regional/object storage | GB-month + operations | 1-10 | 0.015-0.06 | LOW | official Cloud Storage pricing; retention missing |
| Artifact Registry | DEPLOYED | AI 2.12GB, Backend 376MB, Frontend 75.6MB images | GB-month after free tier | 0-1 | <0.01 | MEDIUM | image sizes + official Artifact Registry pricing |
| Network / egress | ESTIMATE | same-region service traffic mostly free; internet egress uncertain | GB egress | 0-5 | 0.005-0.04 | LOW | Cloud Run pricing notes; usage missing |
| Logging / monitoring | DESIGNED_NOT_DEPLOYED | Cloud Logging/Monitoring | ingested logs/metrics and alert resources | 0-5 | 0-0.02 | LOW | CLOUD-07 design; no live monitoring |

## Local performance evidence

| Component | CPU p95 | RAM p95 | Notes |
|---|---:|---:|---|
| Frontend | ~1.98% | ~14.68 MiB | Static/nginx-like serving; Cloud Run min 0. |
| Backend | ~7.67% | ~267.50 MiB | Java runtime; planned 512Mi Cloud Run. |
| AI | ~346.62% | ~801.20 MiB; peak ~940.80 MiB | Main compute consumer; CPU-only local run, no GPU used. |
| Postgres | ~4.13% | ~37.19 MiB | Low single-run load; Cloud SQL micro remains projected. |

Docker image sizes used for planning: AI ~2.12 GB, Backend ~376 MB, Frontend ~75.6 MB.

## Low/base/high cloud estimate

| Level | Compute | Database allocation | Storage | Network/logging | Technical cloud USD/study | Support allocation note |
|---|---:|---:|---:|---:|---:|---|
| LOW | 0.03 | 0.01 | 0.015 | 0.015 | 0.07 | Support remains modeled separately per customer. |
| BASE | 0.08 | 0.03 | 0.03 | 0.02 | 0.16 | Support remains modeled separately per customer. |
| HIGH | 0.20 | 0.08 | 0.06 | 0.04 | 0.38 | Support remains modeled separately per customer. |

Workbook mapping: technical cloud cost is split into `cloud_cost_per_study`, `storage_cost_per_study`, and `ai_processing_cost_per_study`; support allocation remains in `variable_support_per_customer`.

## Caveats

- The AI Cloud Run service is not deployed; AI per-study compute remains ESTIMATED.
- Real inference duration per study is still a missing input.
- Cloud SQL cost is PROJECTED_INFRA_COST, not current spend.
- Pricing and demand are business assumptions, not market-validated values.
- No external willingness-to-pay benchmarking was performed.
