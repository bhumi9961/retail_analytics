"""Data-quality checks against the loaded MySQL database (Part B3, automated).

These run only when MySQL is up; otherwise they are skipped.

TODO (Bhumi): after the pipeline loads data, add checks such as:
    - row counts in MySQL == row counts of the clean CSVs
    - no order_items without a matching order (orphans)
    - no NULL order_id / customer_unique_id
    - RFM segment counts add up to the number of unique customers
"""

import pytest
from sqlalchemy import text

pytestmark = pytest.mark.db


def test_database_is_reachable(db_engine):
    with db_engine.connect() as conn:
        assert conn.execute(text("SELECT 1")).scalar() == 1
