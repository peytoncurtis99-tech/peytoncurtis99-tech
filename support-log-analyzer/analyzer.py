#!/usr/bin/env python3
import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description="Analyze authentication/support logs")
    p.add_argument("logfile", help="CSV file to analyze")
    p.add_argument("--threshold", type=int, default=3, help="Failed login alert threshold")
    p.add_argument("--output", default="report.md", help="Markdown report path")
    return p.parse_args()


def load_rows(path):
    required = {"timestamp", "user", "ip", "event", "status", "reason"}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not required.issubset(reader.fieldnames or []):
            missing = required - set(reader.fieldnames or [])
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        rows = list(reader)
    for row in rows:
        row["_dt"] = datetime.fromisoformat(row["timestamp"])
    return sorted(rows, key=lambda r: r["_dt"])


def analyze(rows, threshold):
    failures_by_user = Counter()
    failures_by_ip = Counter()
    failure_reasons = Counter()
    successes = 0
    failures = 0
    alerts = []
    failure_history = defaultdict(int)

    for row in rows:
        if row["event"] != "login":
            continue
        if row["status"] == "failure":
            failures += 1
            failures_by_user[row["user"]] += 1
            failures_by_ip[row["ip"]] += 1
            failure_reasons[row["reason"]] += 1
            failure_history[(row["user"], row["ip"])] += 1
        elif row["status"] == "success":
            successes += 1
            key = (row["user"], row["ip"])
            if failure_history[key] >= threshold:
                alerts.append(
                    f"Successful login for {row['user']} from {row['ip']} after "
                    f"{failure_history[key]} failures at {row['timestamp']}"
                )
            failure_history[key] = 0

    repeated_users = {k: v for k, v in failures_by_user.items() if v >= threshold}
    repeated_ips = {k: v for k, v in failures_by_ip.items() if v >= threshold}

    return {
        "total": len(rows),
        "successes": successes,
        "failures": failures,
        "repeated_users": repeated_users,
        "repeated_ips": repeated_ips,
        "failure_reasons": failure_reasons,
        "alerts": alerts,
    }


def render_report(result, source):
    lines = [
        "# Authentication Investigation Report",
        "",
        f"**Source:** `{source}`  ",
        f"**Events analyzed:** {result['total']}  ",
        f"**Successful logins:** {result['successes']}  ",
        f"**Failed logins:** {result['failures']}",
        "",
        "## Repeated Failures by User",
    ]
    if result["repeated_users"]:
        lines += [f"- `{k}`: {v} failures" for k, v in sorted(result["repeated_users"].items(), key=lambda x: -x[1])]
    else:
        lines.append("- None above threshold")

    lines += ["", "## Repeated Failures by IP"]
    if result["repeated_ips"]:
        lines += [f"- `{k}`: {v} failures" for k, v in sorted(result["repeated_ips"].items(), key=lambda x: -x[1])]
    else:
        lines.append("- None above threshold")

    lines += ["", "## Failure Reasons"]
    if result["failure_reasons"]:
        lines += [f"- {k}: {v}" for k, v in result["failure_reasons"].most_common()]
    else:
        lines.append("- No failed-login reasons found")

    lines += ["", "## Correlation Alerts"]
    if result["alerts"]:
        lines += [f"- {a}" for a in result["alerts"]]
    else:
        lines.append("- No success-after-failure patterns detected")

    lines += [
        "",
        "## Suggested Investigation Steps",
        "1. Verify whether affected users expected the authentication attempts.",
        "2. Compare source IPs with known devices, VPN ranges, or approved locations.",
        "3. Review MFA and identity-provider events around the same timestamps.",
        "4. Check for lockouts, password resets, token refresh failures, or device posture failures.",
        "5. Escalate if activity cannot be explained by expected user behavior.",
    ]
    return "\n".join(lines) + "\n"


def main():
    args = parse_args()
    rows = load_rows(args.logfile)
    result = analyze(rows, args.threshold)
    report = render_report(result, args.logfile)
    Path(args.output).write_text(report, encoding="utf-8")
    print(report)
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
