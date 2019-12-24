from tools.nasa_api import download_image, os
import pytest
from os import path
import sys


@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_path_exists(*args, **kwargs):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_path_exists)


def test_img_path(DATE_IMG):
    expected = '2019-12-24_A-Northern-Winter-Sky-Panorama.jpg'
    assert expected in download_image(date=DATE_IMG)


def test_img_cached(DATE_IMG, mock_os_path_exists, capsys):
    img_path = download_image(date=DATE_IMG)
    captured = capsys.readouterr()
    assert "Today's img already downloaded, setting as background" in captured[
        0]
