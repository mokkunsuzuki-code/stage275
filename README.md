# Stage275: Key Usage Policy

## Overview

Stage275 introduces explicit key usage policy for QSP.

This stage defines:

- who may use keys
- which keys may be used
- what actions are allowed
- what conditions must be satisfied before signing or approval

It extends Stage274.

## Files

- `policy/key_usage_policy.yaml`
- `docs/key_usage_policy.md`
- `tools/verify_key_usage_policy.py`
- `out/key_usage_policy_evidence.json`

## Actors

- CI
- Human reviewer
- Future YubiKey holder

## Key Classes

- CI managed key
- Human approval key
- Future YubiKey approval key

## What This Stage Adds

- explicit actor separation
- explicit signing conditions
- explicit forbidden actions
- future YubiKey integration path

## Evidence

Run:

```bash
python3 tools/verify_key_usage_policy.py

This generates:

out/key_usage_policy_evidence.json
Security Meaning

Before this stage, the project defined where keys are protected.

This stage defines how keys may be used.

That means trust is no longer based only on possession of keys,
but also on policy, approval path, and actor separation.

Limitations

This stage does NOT yet prove live hardware-token approval.

YubiKey integration remains pending.

License

MIT License
