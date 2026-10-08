# Test strategy

> TODO (Bhumi): fill this in as you build. Interviewers like this file - it shows
> you think like a tester, which is your background.

| Layer | What it checks | Where | Needs DB? |
|---|---|---|---|
| Unit | Each cleaning rule on tiny hand-made data | `tests/unit/` | No |
| Data quality | Row counts, orphans, nulls, totals after loading | `tests/data_quality/` | Yes |
| SQL views | Views return expected columns and consistent totals | `tests/data_quality/` | Yes |

## How to run
    pytest                      # everything (DB tests skip if MySQL is down)
    pytest -m "not db"          # only fast tests
    pytest --cov=retail         # with coverage report

## Test cases and edge cases I considered
- ...
