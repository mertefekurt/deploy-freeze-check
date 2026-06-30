# deploy-freeze-check

**Evaluator Format.** Check deployment plans for freeze windows, approvals, and rollback readiness.

## Objective

Deployments during risky windows need explicit controls. This CLI flags release plans that lack approval or rollback coverage.

## Evaluation Criteria

`deploy-freeze-check` accepts deployment plan, release calendar, or change request text in text, JSON, JSONL, or CSV form.

## Commands

```bash
python -m pip install -e ".[dev]"
deploy-freeze-check examples/sample.txt
deploy-freeze-check examples/sample.txt --json --fail-on medium
```

## Artifacts

| Rule | Severity | Meaning |
|---|---:|---|
| `freeze-active` | high | deployment overlaps a freeze window |
| `missing-approval` | medium | approval is missing |
| `unknown-rollback` | low | rollback readiness is unclear |

## License

```bash
ruff check .
pytest
python -m deploy_freeze_check --help
```

License: MIT

### Example Input

```text
deploy friday 18:00 freeze active approval missing rollback unknown
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the deploy-freeze-check policy surface explicit.
