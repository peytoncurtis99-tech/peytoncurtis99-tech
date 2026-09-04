# Support Log Analyzer

A lightweight Python command-line tool for support and security investigations. It parses structured authentication/application logs, identifies repeated failures, flags suspicious patterns, and produces a concise report an engineer can use during triage.

## Why I Built It

Support engineers often start with messy logs and an unclear report such as “login is broken.” This project demonstrates a repeatable workflow for turning raw events into useful investigation signals.

## Features

- Parses CSV logs
- Counts successful and failed authentication attempts
- Groups failures by user, IP address, and reason
- Flags repeated failed logins using a configurable threshold
- Detects successful login after repeated failures
- Produces a Markdown incident summary
- Uses only the Python standard library

## Example

```bash
python analyzer.py sample_logs.csv --threshold 3 --output report.md
```

## Skills Demonstrated

Python, log analysis, authentication troubleshooting, incident triage, support automation, structured reporting, defensive security analysis.

## Next Steps

- JSON and syslog ingestion
- Time-window correlation
- Geo/IP enrichment using an approved internal source
- SIEM export format
- Unit tests and CI validation
