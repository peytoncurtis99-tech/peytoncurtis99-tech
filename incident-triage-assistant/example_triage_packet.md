# Triage Packet

## Recommended Severity
SEV-2

## Reported Issue
Multiple users cannot login to the internal developer portal after the morning access-policy update. MFA completes but the portal returns HTTP 403. One affected account is engineer@example.com and the source test IP was 10.20.30.40. There is customer impact but no confirmed security incident.

## Extracted Indicators
- IPs: 10.20.30.40
- Accounts: engineer@example.com
- Error codes: HTTP 403

## Investigation Checklist
1. Confirm scope: one user, a group, or service-wide.
2. Confirm exact timestamps and timezone.
3. Check recent configuration, deployment, identity, or policy changes.
4. Review authentication/application logs for the affected account and source device.
5. Verify MFA, token, session, entitlement, and device-posture state where applicable.
6. Reproduce safely if possible and record what changes the outcome.
7. Document findings, workaround, owner, and next update time.

## Escalation Triggers
- Broad production impact
- Security or privacy concern
- Suspected unauthorized access
- Data loss or corruption
- Repeated failure without a safe workaround

## Draft Runbook Note
**Symptom:** [summarize observed behavior]

**Evidence:** [logs, timestamps, accounts, errors]

**Checks performed:** [steps]

**Resolution/workaround:** [result]

**Follow-up:** [owner and prevention step]
