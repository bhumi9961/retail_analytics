"""Shared test fixtures: tiny hand-made DataFrames that mimic the Olist columns.

Small fixtures make tests fast and make it obvious what each test checks.
Add more fixtures here as you need them.
"""

import pandas as pd
import pytest
from sqlalchemy import Engine

from retail.config import get_settings
from retail.load import check_connection, get_engine


@pytest.fixture
def order_items() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2", "o3"],
            "order_item_id": [1, 2, 1, 1],
            "product_id": ["p1", "p2", "p1", "p3"],
            "seller_id": ["s1", "s1", "s2", "s3"],
            "price": [50.0, 0.0, 20.5, -3.0],
            "freight_value": [10.0, 5.0, 4.5, 2.0],
        }
    )


@pytest.fixture
def payments() -> pd.DataFrame:
    # o1 was paid in two parts (voucher + credit card)
    return pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2"],
            "payment_sequential": [2, 1, 1],
            "payment_type": ["voucher", "credit_card", "boleto"],
            "payment_installments": [1, 3, 1],
            "payment_value": [20.0, 45.0, 25.0],
        }
    )


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    """A database engine, or skip the test if MySQL is not running."""
    engine = get_engine(get_settings())
    if not check_connection(engine):
        pytest.skip("MySQL not running (start it with: docker compose up -d)")
    return engine
