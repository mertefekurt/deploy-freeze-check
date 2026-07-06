<img src="assets/readme-cover.svg" alt="Deploy Freeze Check cover" width="100%" />

# Deploy Freeze Check

Check deployment plans for freeze windows, approvals, and rollback readiness.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `deploy-freeze-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `freeze-active` | high | deployment overlaps a freeze window |
| `missing-approval` | medium | approval is missing |
| `unknown-rollback` | low | rollback readiness is unclear |

## Command line

```bash
python -m pip install -e ".[dev]"
deploy-freeze-check examples/sample.txt
deploy-freeze-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
deploy friday 18:00 freeze active approval missing rollback unknown
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
