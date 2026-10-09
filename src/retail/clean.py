"""Step 2 of the pipeline: cleaning rules (Part A of the guideline).

Each rule is its own small function so it can be unit-tested on a tiny DataFrame.
Every function takes a DataFrame and returns a NEW DataFrame (never edit the input).

TODO (Bhumi): implement these one at a time, writing a test in
tests/unit/test_clean.py for each before moving on.
"""

from __future__ import annotations

import pandas as pd

ORDER_DATE_COLUMNS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


# ---------- single-table rules ----------

def drop_nonpositive_prices(items: pd.DataFrame) -> pd.DataFrame:
    """Remove order items whose price is <= 0. Rows with a missing price are also removed."""
    valid_items = items[items["price"] > 0]
    return valid_items.copy()

def parse_order_dates(orders: pd.DataFrame) -> pd.DataFrame:
    """Convert the date columns in ORDER_DATE_COLUMNS from text to datetime.

    Invalid values should become NaT, not crash. Hint: pd.to_datetime(errors="coerce")
    """
    raise NotImplementedError


def remove_orders_without_purchase_date(orders: pd.DataFrame) -> pd.DataFrame:
    """Drop orders where order_purchase_timestamp is missing."""

    return orders[orders["order_purchase_timestamp"].notna()].copy() 


def tidy_city_names(customers: pd.DataFrame) -> pd.DataFrame:
    """Trim spaces and convert customer_city to Title Case."""
    raise NotImplementedError


def combine_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """One row per order: total payment_value, first payment_type
    (lowest payment_sequential), max payment_installments.
    """
    raise NotImplementedError


def latest_review_per_order(reviews: pd.DataFrame) -> pd.DataFrame:
    """Keep only the most recent review for each order_id."""
    raise NotImplementedError


def add_delivery_metrics(orders: pd.DataFrame) -> pd.DataFrame:
    """Add delivery_days, delay_days and is_late columns.

    delivery_days = delivered_customer_date - purchase_timestamp (in days)
    delay_days    = delivered_customer_date - estimated_delivery_date (in days)
    is_late       = delay_days > 0
    Orders that were never delivered should get missing values, not 0.
    """
    raise NotImplementedError


def translate_categories(products: pd.DataFrame, translation: pd.DataFrame) -> pd.DataFrame:
    """Add the English category name; fill missing categories with "unknown"."""
    raise NotImplementedError


# ---------- build the two final tables (Part A5) ----------

def build_orders_clean(frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """orders_clean: one row per order with customer_unique_id, city, state, status,
    dates, delivery_days, delay_days, is_late, review score, payment type,
    installments and payment value.
    """
    raise NotImplementedError


def build_order_items_clean(frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """order_items_clean: one row per item with order_id, order_item_id, product_id,
    seller_id, English category name, price and freight_value.
    """
    raise NotImplementedError
