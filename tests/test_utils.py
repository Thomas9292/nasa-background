from datetime import datetime

from tools.utils import parse_str_to_date


"""
Tests for parse_str_to_date()
"""
def test_parse_str_to_date_short():
    try:
        parse_str_to_date("190706")
        assert 1 == 0
    except Exception as e:
        assert isinstance(e, ValueError), "Should throw value error on short string."


def test_parse_str_to_date_incomplete():
    try:
        parse_str_to_date("2019-07")
        assert 1 == 0
    except Exception as e:
        assert isinstance(e, ValueError), "Should throw value error on short string."


def test_parse_str_to_date_full():
    assert parse_str_to_date("20190706") == datetime(2019, 7, 6)


def test_parse_str_to_date_minified():
    assert parse_str_to_date("2019-7-6") == datetime(2019, 7, 6)


def test_parse_str_to_date_extra():
    assert parse_str_to_date("2019-7-6-9-12-3-34-5-1") == datetime(2019, 7, 6)
