"""Command-line entry point.

    python -m retail.pipeline profile   # Part A1: inspect the raw files
    python -m retail.pipeline clean     # build clean CSVs only (no database needed)
    python -m retail.pipeline run       # clean + load into MySQL + create views
    python -m retail.pipeline check-db  # test the database connection
"""

from __future__ import annotations

import argparse
import logging
import sys

from retail import clean, extract, load
from retail.config import PROJECT_ROOT, get_settings

SQL_DIR = PROJECT_ROOT / "sql"
log = logging.getLogger("retail")


def build_clean_tables(settings) -> dict:
    frames = extract.load_raw(settings.raw_dir)
    tables = {
        "orders": clean.build_orders_clean(frames),
        "order_items": clean.build_order_items_clean(frames),
    }
    for name, df in tables.items():
        load.save_csv(df, settings.clean_dir, f"{name}_clean")
    return tables


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="retail", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["profile", "clean", "run", "check-db"])
    args = parser.parse_args(argv)

    settings = get_settings()
    logging.basicConfig(level=settings.log_level,
                        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s")

    if args.command == "profile":
        for name, df in extract.load_raw(settings.raw_dir).items():
            log.info("%s: %s", name, extract.profile(df))
        return 0

    if args.command == "check-db":
        ok = load.check_connection(load.get_engine(settings))
        log.info("Database reachable: %s", ok)
        return 0 if ok else 1

    tables = build_clean_tables(settings)
    if args.command == "clean":
        return 0

    # command == "run"
    engine = load.get_engine(settings)
    if not load.check_connection(engine):
        log.error("Start the database first:  docker compose up -d")
        return 1
    load.run_sql_file(engine, SQL_DIR / "schema.sql")
    for name, df in tables.items():
        n = load.load_table(engine, df, name)
        log.info("Loaded %s: %d rows", name, n)
    load.run_sql_file(engine, SQL_DIR / "views.sql")
    log.info("Pipeline finished.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
