# Retail Sales & Customer Intelligence Analytics

![CI](https://github.com/<your-username>/retail-analytics/actions/workflows/ci.yml/badge.svg)

An end-to-end, **tested** data pipeline and analytics app for ~100K e-commerce orders
from the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

> Started as an internship project (see [`internship-v1/`](internship-v1/)), then rebuilt
> as software: modular Python, automated MySQL loading, pytest suite, Docker and CI.

## Business questions
1. Which customers drive revenue, and how many come back? (RFM, cohorts)
2. How do late deliveries affect review scores?
3. Which states, categories and sellers matter most?

## Architecture
```
data/raw/*.csv  ->  extract.py  ->  clean.py  ->  data/cleaned/*.csv
                                         |
                                         v
                           load.py -> MySQL (schema.sql) -> views.sql
                                                         |
                                         Excel / Power BI / app (coming)
```

## Project structure
```
src/retail/        pipeline code (config, extract, clean, load, pipeline CLI)
sql/               schema.sql (tables) and views.sql (analysis views)
tests/unit/        fast tests for each cleaning rule
tests/data_quality checks against the loaded database
app/               dashboard / API (Phase 5)
docs/TESTING.md    test strategy
internship-v1/     original internship deliverables
```

## Getting started
Requirements: Python 3.10+, Docker Desktop, Git.

```bash
# 1. Get the code and install
git clone https://github.com/bhumi9961/retail_analytics.git
cd retail_analytics
python -m venv .venv
# Windows: .venv\Scripts\activate      Mac/Linux: source .venv/bin/activate
pip install -e ".[dev]"

# 2. Settings
cp .env.example .env          # Windows: copy .env.example .env

# 3. Data: download from Kaggle and unzip the 9 CSVs into data/raw/

# 4. Database
docker compose up -d
python -m retail.pipeline check-db

# 5. Run
python -m retail.pipeline profile   # inspect raw data
python -m retail.pipeline run       # clean -> load -> views

# 6. Test
pytest
ruff check .
```

## Key findings
_TODO: 3-5 findings with numbers, e.g. "Orders 8+ days late average X stars vs Y on time."_

## Design decisions
_TODO: why views instead of raw tables, why customer_unique_id, what you would change if
the data doubled (incremental loads, indexes, partitioning, a cloud warehouse)._

## Tech stack
Python, pandas, SQLAlchemy, MySQL 8, Docker, pytest, Ruff, GitHub Actions, Excel, Power BI
