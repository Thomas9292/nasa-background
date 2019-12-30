import datetime

import pytest


@pytest.fixture
def DATE_VID():
    return datetime.datetime.strptime("2019-12-23", "%Y-%m-%d")


@pytest.fixture
def DATE_IMG():
    return datetime.datetime.strptime("2019-12-24", "%Y-%m-%d")
