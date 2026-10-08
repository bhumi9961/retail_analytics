"""Step 1 of the pipeline: read the raw Olist CSV files."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

log = logging.getLogger(__name__)

# Short name used in code  ->  file name from Kaggle
RAW_FILES: dict[str, str] = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def load_raw(raw_dir: Path) -> dict[str, pd.DataFrame]:
    """Read all 7 raw CSVs into a dict of DataFrames, keyed by short name."""
    missing = [f for f in RAW_FILES.values() if not (raw_dir / f).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing files in {raw_dir}: {missing}. "
            "Download the Olist dataset from Kaggle and unzip it into data/raw/."
        )

    frames = {name: pd.read_csv(raw_dir / file) for name, file in RAW_FILES.items()}
    for name, df in frames.items():
        log.info("Loaded %-22s %8d rows", name, len(df))
    return frames


def profile(df: pd.DataFrame) -> dict[str, object]:
    """Summarise one DataFrame: row count, nulls per column, duplicate rows.

    This is Part A1 of the guideline ("Load and inspect").

    TODO (Bhumi): return a dict like
        {"rows": 99441, "duplicates": 0, "nulls": {"order_approved_at": 160, ...}}
    Only include columns that actually have nulls.
    Hint: len(df), df.duplicated().sum(), df.isna().sum()
    """
    raise NotImplementedError
