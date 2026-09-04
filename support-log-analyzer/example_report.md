# Authentication Investigation Report

**Source:** `support-log-analyzer/sample_logs.csv`  
**Events analyzed:** 10  
**Successful logins:** 2  
**Failed logins:** 8

## Repeated Failures by User
- `alice`: 3 failures
- `dave`: 3 failures

## Repeated Failures by IP
- `10.10.1.10`: 3 failures
- `203.0.113.25`: 3 failures

## Failure Reasons
- bad_password: 3
- device_posture: 3
- mfa_denied: 2

## Correlation Alerts
- Successful login for alice from 10.10.1.10 after 3 failures at 2026-09-04T08:01:02

## Suggested Investigation Steps
1. Verify whether affected users expected the authentication attempts.
2. Compare source IPs with known devices, VPN ranges, or approved locations.
3. Review MFA and identity-provider events around the same timestamps.
4. Check for lockouts, password resets, token refresh failures, or device posture failures.
5. Escalate if activity cannot be explained by expected user behavior.
