from collar_metrics.barks_table import BarksTable
import pytest
import time


@pytest.fixture(scope="module")
def barks_table():
    t = BarksTable()
    t.gracefully_create_table()
    return t


def test_adding_a_bark_increases_len(barks_table):
    n = len(barks_table.by_collar('1'))
    barks_table.add(collar='1', timestamp="2019-03-01", volume='3')
    assert len(barks_table.by_collar('1')) == (n + 1)
