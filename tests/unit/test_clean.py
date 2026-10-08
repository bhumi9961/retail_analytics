"""Unit tests for the cleaning rules in src/retail/clean.py.

Pattern for every test (Arrange - Act - Assert):
    1. Arrange: take a small fixture DataFrame (see conftest.py)
    2. Act:     call ONE cleaning function
    3. Assert:  check the exact rows / values you expect

TODO (Bhumi): your first task - remove the skip below, implement
drop_nonpositive_prices() in clean.py, and make this test pass. Then add more
tests, e.g.:
    - the input DataFrame is not modified
    - an empty DataFrame returns an empty DataFrame
    - combine_payments: o1 -> total 65.0, first type "credit_card", max installments 3
"""

import pytest

from retail.clean import drop_nonpositive_prices


@pytest.mark.skip(reason="TODO: implement drop_nonpositive_prices first")
def test_drop_nonpositive_prices_removes_zero_and_negative(order_items):
    result = drop_nonpositive_prices(order_items)

    assert (result["price"] > 0).all()
    assert len(result) == 2
