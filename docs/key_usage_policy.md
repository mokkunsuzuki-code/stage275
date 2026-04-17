# Stage275: Key Usage Policy

## Overview

Stage275 defines how keys may be used, by whom, and under which conditions.

This stage extends Stage274.

Stage274 answered:

- where keys are protected

Stage275 answers:

- who may use keys
- for what purpose
- under what approval conditions

## Actors

- CI
- Human reviewer
- Future YubiKey holder

## Core Idea

Different trust levels require different approval paths.

### CI

CI may sign:

- CI evidence
- build summaries
- verification results

CI may NOT claim human approval.

### Human reviewer

A human reviewer may approve:

- release approval
- external submission
- security claims

### YubiKey holder (future)

A YubiKey-backed actor will be reserved for highest-trust approvals.

## What This Stage Proves

- key usage is policy-bound
- actor separation is explicit
- future hardware approval path is defined

## Limitations

This stage does NOT yet prove live YubiKey approval.

That will be added after hardware integration.
