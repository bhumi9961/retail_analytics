"""Step 3 of the pipeline: write clean data to CSV and MySQL, then create views."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
from sqlalchemy import Engine, create_engine, text

from retail.config import Settings

log = logging.getLogger(__name__)


def get_engine(settings: Settings) -> Engine:
    """Create a SQLAlchemy engine for the MySQL database."""
    return create_engine(settings.db_url, pool_pre_ping=True)


def check_connection(engine: Engine) -> bool:
    """Return True if the database answers a simple query."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception as exc:  # noqa: BLE001 - we just want a yes/no here
        log.error("Database connection failed: %s", exc)
        return False


def run_sql_file(engine: Engine, path: Path) -> None:
    """Execute every statement in a .sql file (statements separated by ';').

    Keep sql files simple: no ';' inside strings or comments.
    """
    statements = [s.strip() for s in path.read_text(encoding="utf-8").split(";")]
    with engine.begin() as conn:
        for stmt in statements:
            if stmt and not all(line.strip().startswith("--") for line in stmt.splitlines()):
                conn.execute(text(stmt))
    log.info("Ran %s", path.name)


def save_csv(df: pd.DataFrame, clean_dir: Path, name: str) -> Path:
    """Save a clean table to data/cleaned/<name>.csv (Part A6)."""
    clean_dir.mkdir(parents=True, exist_ok=True)
    out = clean_dir / f"{name}.csv"
    df.to_csv(out, index=False)
    log.info("Saved %s (%d rows)", out.name, len(df))
    return out


def load_table(engine: Engine, df: pd.DataFrame, table: str) -> int:
    """Insert a DataFrame into an EXISTING MySQL table (created by sql/schema.sql).

    TODO (Bhumi): empty the table first (TRUNCATE or DELETE), then insert the rows,
    and return the number of rows inserted. Do NOT let pandas create the table -
    the schema (types, keys) must come from schema.sql.
    Hint: df.to_sql(table, engine, if_exists="append", index=False, chunksize=5000)
    """
    raise NotImplementedError
