# Identity & Access Lab

A practical learning lab for identity, authentication, authorization, and access troubleshooting. This repository documents concepts and investigation procedures rather than claiming production enterprise administration experience.

## Objectives

- Understand authentication vs. authorization
- Learn SSO and federation concepts
- Compare SAML 2.0 and OAuth 2.0 / OpenID Connect
- Understand MFA, phishing-resistant MFA, FIDO2, and WebAuthn
- Practice investigating login failures from logs and user reports
- Build repeatable support runbooks
- Learn least privilege, access reviews, session/token concepts, and device posture

## Lab Scenarios

### Scenario 1: Password Works, SSO Fails
Investigate identity-provider availability, redirect URI configuration, certificate/metadata changes, user assignment, clock skew, and application logs.

### Scenario 2: MFA Succeeds, Application Returns 403
Separate authentication from authorization. Verify group membership, application role mapping, entitlements, policy evaluation, token claims, and recent access-policy changes.

### Scenario 3: User Repeatedly Reauthenticates
Check session duration, token expiration, refresh-token behavior, browser/device state, cookies, conditional access, and time synchronization.

### Scenario 4: Device Is Blocked
Review device posture requirements, endpoint health signals, certificate state, OS compliance, EDR status, and conditional access policy.

## Runbook Template

See [`RUNBOOK_TEMPLATE.md`](RUNBOOK_TEMPLATE.md).

## Investigation Principles

1. Establish scope before changing anything.
2. Record timestamps and timezone.
3. Separate authentication failure from authorization failure.
4. Compare expected policy with actual evaluated policy.
5. Use logs to verify assumptions.
6. Prefer reversible changes during troubleshooting.
7. Document the resolution and prevention step.

## Roadmap

- Build a local Active Directory test environment
- Add an identity provider sandbox
- Configure a test OIDC application
- Capture sample authentication logs
- Automate log parsing with Python
- Add diagrams for SAML and OIDC request flows
