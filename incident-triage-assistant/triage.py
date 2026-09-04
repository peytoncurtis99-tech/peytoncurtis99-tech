#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

SEVERITY_RULES = [
    ("SEV-1", ["outage", "all users", "production down", "security breach", "data loss"]),
    ("SEV-2", ["multiple users", "cannot login", "authentication failure", "degraded", "customer impact"]),
    ("SEV-3", ["single user", "intermittent", "workaround", "how do i", "request"]),
]


def recommend_severity(text):
    lower = text.lower()
    for severity, terms in SEVERITY_RULES:
        if any(term in lower for term in terms):
            return severity
    return "SEV-3"


def extract_indicators(text):
    ips = sorted(set(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)))
    emails = sorted(set(re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text)))
    error_codes = sorted(set(re.findall(r"\b(?:ERR|ERROR|HTTP)[-_ ]?\d{3,5}\b", text, re.I)))
    return ips, emails, error_codes


def build_packet(text):
    severity = recommend_severity(text)
    ips, emails, error_codes = extract_indicators(text)
    return f"""# Triage Packet

## Recommended Severity
{severity}

## Reported Issue
{text.strip()}

## Extracted Indicators
- IPs: {', '.join(ips) if ips else 'None found'}
- Accounts: {', '.join(emails) if emails else 'None found'}
- Error codes: {', '.join(error_codes) if error_codes else 'None found'}

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
**Symptom:** [summarize observed behavior]\n\n**Evidence:** [logs, timestamps, accounts, errors]\n\n**Checks performed:** [steps]\n\n**Resolution/workaround:** [result]\n\n**Follow-up:** [owner and prevention step]
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ticket")
    parser.add_argument("--output", default="triage_packet.md")
    args = parser.parse_args()
    text = Path(args.ticket).read_text(encoding="utf-8")
    packet = build_packet(text)
    Path(args.output).write_text(packet, encoding="utf-8")
    print(packet)


if __name__ == "__main__":
    main()
