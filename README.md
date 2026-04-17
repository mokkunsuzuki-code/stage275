# Stage276: CI Evidence Automation

## Overview

Stage276 introduces automated CI evidence generation for QSP.

This stage automatically collects and bundles:

- run information
- artifact information
- verification results
- summary output

using GitHub Actions.

This moves the project from:

- defining verification

to:

- automatically executing verification in CI
- preserving the resulting evidence as artifacts

## Files

- `.github/workflows/stage276-ci-evidence.yml`
- `docs/stage276_ci_evidence.md`
- `tools/build_stage276_summary.py`
- `tools/verify_stage276_evidence.py`
- `out/ci_evidence/stage276_summary.json`
- `out/ci_evidence/verify_stage276_result.json`

## What This Stage Adds

- automatic CI summary generation
- automatic verification result generation
- GitHub Actions artifact upload
- structured CI evidence for later review

## Local Run

You can run the evidence generation locally:

```bash
python3 tools/build_stage276_summary.py
python3 tools/verify_stage276_evidence.py
Generated Evidence

This stage generates:

out/ci_evidence/stage276_summary.json
out/ci_evidence/verify_stage276_result.json
stage276_summary.json

Records structured CI-related information, including:

run ID
run number
workflow name
commit SHA
ref
actor
artifact file references
verify_stage276_result.json

Records structured verification output, including:

whether the summary exists
whether run information is present
whether artifact information is present
whether expected references are present
overall verification result
GitHub Actions

The workflow:

checks out the repository
sets up Python
generates the CI summary
verifies the generated evidence
uploads the resulting files as an artifact

Workflow file:

.github/workflows/stage276-ci-evidence.yml
Security Meaning

Before this stage, the project defined:

how keys are protected
how keys may be used

Stage276 adds:

proof that verification actually ran in CI
proof that evidence was automatically generated
proof that artifacts were preserved for later inspection

This means trust is no longer based only on documentation and policy,
but also on reproducible CI execution evidence.

What This Stage Proves
CI execution is real
verification output is structured
evidence can be generated automatically
CI artifacts can be preserved for review
Limitations

This stage does NOT yet prove:

external independent re-execution
external attestation beyond GitHub Actions
hardware-backed approval execution

Those can be added in later stages.

Position in QSP

Stage274 introduced:

key protection structure

Stage275 introduced:

key usage policy

Stage276 introduces:

automated CI execution evidence

Together, these stages form:

protection
policy
execution evidence
License

MIT License
