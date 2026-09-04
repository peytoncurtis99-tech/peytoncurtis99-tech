# Authentication / Access Incident Runbook

## 1. Intake
- User/account:
- Application/service:
- Start time and timezone:
- Scope:
- Exact error:
- Recent changes:

## 2. Determine Failure Stage
- Identity lookup
- Primary authentication
- MFA
- Federation / token issuance
- Application session
- Authorization / entitlement
- Device posture / conditional access

## 3. Evidence
- Identity-provider logs:
- Application logs:
- Source IP/device:
- Token/claim information (never paste secrets):
- Policy result:

## 4. Safe Checks
- Confirm account status
- Confirm application assignment
- Confirm group/role membership
- Confirm MFA enrollment/state
- Confirm device compliance
- Confirm redirect URI / metadata / certificate configuration
- Confirm timestamps and clock synchronization

## 5. Resolution
- Root cause:
- Change made:
- Validation performed:
- User impact restored at:

## 6. Follow-up
- Documentation update:
- Automation opportunity:
- Product friction identified:
- Prevention action / owner:
