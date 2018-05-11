from collar_metrics.barks_table import BarksTable


def test_empty_table_has_no_barks():
    barks = BarksTable()
    assert not len(barks.by_collar(1))


def test_adding_a_bark_increases_len():
    barks = BarksTable()
    barks.add(collar=1, timestamp="2018-03-01")
    assert len(barks.by_collar(1)) == 1
