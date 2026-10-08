# M08.P02 — Release Gate Worksheet

## Candidate release

```text
release_id:
app_version:
git_commit:
model_id:
prompt_version:
index_version:
policy_version:
eval_suite_version:
thresholds_version:
```

## Change risk table

| Change | Artifact | Risk | Failure mode | Required evidence | Owner | Rollback unit |
|---|---|---:|---|---|---|---|
| | | | | | | |

## Required quality gates

| Gate | Required? | Applies to which change? | Evidence | Pass/Fail |
|---|---|---|---|---|
| unit_tests | | | | |
| schema_tests | | | | |
| policy_tests | | | | |
| prompt_eval | | | | |
| retrieval_eval | | | | |
| model_eval | | | | |
| security_eval | | | | |
| authorization_tests | | | | |
| cost_latency_eval | | | | |
| human_approval | | | | |
| rollback_plan | | | | |

## Promotion strategy

```text
DEV -> STAGING -> EVAL -> APPROVAL -> ______ -> PROD
```

For each relevant change:

| Change | CANARY | SHADOW | DIRECT_PROMOTION | DO_NOT_PROMOTE | Reason |
|---|---|---|---|---|---|
| | | | | | |

## Rollback target

```text
release_id:
model_id:
prompt_version:
index_version:
policy_version:
conditions_that_trigger_rollback:
rollback_authority:
```

## Platform split

| Capability | SHARED_PLATFORM | PRODUCT_OWNED | SHARED_WITH_PRODUCT_OWNER | Owner of outcome | Reason |
|---|---|---|---|---|---|
| | | | | | |

## Trace contract

| Field | KEEP | REDACT | DROP | Retention | Access |
|---|---|---|---|---|---|
| trace_id | | | | | |
| user_id | | | | | |
| user_email | | | | | |
| prompt_text | | | | | |
| model_id | | | | | |
| prompt_version | | | | | |
| source_ids | | | | | |
| tool_calls | | | | | |
| tokens | | | | | |
| latency | | | | | |
| outcome | | | | | |
| api_key | | | | | |

## Inject decisions

### Inject 1

```text
Decision before inject:
New evidence:
Revised decision:
Reason:
```

### Inject 2

```text
Decision before inject:
New evidence:
Revised decision:
Reason:
```

## Final release decision

```text
PROMOTE / PROMOTE_WITH_CONDITIONS / HOLD / REJECT

Rationale:
Conditions:
Evidence that would change the decision:
```
