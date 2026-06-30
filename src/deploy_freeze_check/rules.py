from __future__ import annotations

from deploy_freeze_check.models import Rule

PROJECT_NAME = 'deploy-freeze-check'
SUMMARY = 'Check deployment plans for freeze windows, approvals, and rollback readiness.'
SAMPLE_RISK = 'deploy friday 18:00 freeze active approval missing rollback unknown'
SAMPLE_CLEAN = 'deploy tuesday 10:00 freeze clear approval change-board rollback documented'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='freeze-active',
        severity='high',
        pattern='\\bfreeze active\\b',
        message='deployment overlaps a freeze window',
        recommendation='Get exception approval or reschedule.',
    ),
    Rule(
        code='missing-approval',
        severity='medium',
        pattern='\\bapproval\\s*(missing|none|null)\\b',
        message='approval is missing',
        recommendation='Record approver and change ticket.',
    ),
    Rule(
        code='unknown-rollback',
        severity='low',
        pattern='\\brollback\\s*(unknown|missing|none)\\b',
        message='rollback readiness is unclear',
        recommendation='Attach rollback plan and owner.',
    ),
)
