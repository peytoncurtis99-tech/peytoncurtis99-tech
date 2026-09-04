# Incident Triage Assistant

A local support-engineering tool that converts an unstructured support ticket into a consistent triage packet: severity recommendation, key facts, investigation checklist, escalation triggers, and a draft runbook note.

This project intentionally runs locally and does not send ticket content to an external model. The output can be used as a structured input for an approved GenAI workflow later.

## Why I Built It

Good support engineering is not just fixing a problem. It is reducing ambiguity, documenting evidence, communicating status, and making future incidents easier to resolve.

## Usage

```bash
python triage.py sample_ticket.txt
```

## Skills Demonstrated

Python, support operations, incident triage, structured outputs, documentation, privacy-aware AI workflow design, automation.
