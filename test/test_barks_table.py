from collar_metrics.barks_table import BarksTable
import pytest


@pytest.fixture(scope="module")
def barks_table():
    t = BarksTable()
    t.gracefully_create_table()
    return t


def test_empty_table_has_no_barks(barks_table):
    assert not len(barks_table.by_collar('1'))


def test_adding_a_bark_increases_len(barks_table):
    barks_table.add(collar='1', timestamp="2018-03-01")
    assert len(barks_table.by_collar('1')) == 1
