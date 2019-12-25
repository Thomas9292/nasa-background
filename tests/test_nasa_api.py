import datetime

import pytest

from tools.nasa_api import download_image, get_info, os

"""
Tests for get_info()
"""
def test_get_info_specific_date():
    # Define the answer for 2019-12-23
    correct_info = {
        'date': '2019-12-23',
        'explanation': "Where is the best place to collect a surface sample from asteroid Bennu?  Launched in 2016, NASA sent the robotic Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer (OSIRIS-REx) to investigate the 500-meter-across asteroid 101955 Bennu. After mapping the near-Earth asteroid's dark surface, OSIRIS-REx will next touch Bennu's surface in 2020 August to collect a surface sample.  The featured 23-second time-lapse video shows four candidate locations for the touch, from which NASA chose just one earlier this month. NASA chose the Nightingale near Bennu's northern hemisphere as the primary touch-down spot because of its relative flatness, lack of boulders, and apparent abundance of fine-grained sand.  Location Osprey is the backup.  NASA plans to return soil samples from Bennu to Earth in 2023 for a detailed analysis.    Free Presentation: APOD Editor to show best astronomy images of 2019 -- and the decade -- in NYC on January 3",
        'media_type': 'video',
        'service_version': 'v1',
        'title': 'Places for OSIRIS-REx to Touch Asteroid Bennu',
        'url': 'https://www.youtube.com/embed/pvKEG141GmU?rel=0'
    }

    # Obtain given answer
    DATE = datetime.datetime.strptime("2019-12-23", "%Y-%m-%d")
    obtained_info = get_info(DATE)

    assert obtained_info == correct_info


"""
Tests for download_image()
"""
@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_path_exists(*args, **kwargs):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_path_exists)


def test_img_path(DATE_IMG):
    expected = '2019-12-24_A-Northern-Winter-Sky-Panorama.jpg'
    img_path = download_image(date=DATE_IMG)
    assert expected in img_path
    assert os.path.exists(img_path)


def test_img_cached(DATE_IMG, mock_os_path_exists, capsys):
    img_path = download_image(date=DATE_IMG)
    captured = capsys.readouterr()
    assert "Today's image has already been downloaded and is now being set as background." in captured[
        0]
