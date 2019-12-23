import datetime

from tools.nasa_api import get_info


def test_get_info():
    # Define the answer for 2019-12-23
    correct_info = {
        'date': '2019-12-23',
        'explanation': "Where is the best place to collect a surface sample from asteroid Bennu?  Launched in 2016, NASA sent the robotic Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer (OSIRIS-REx) to investigate the 500-meter-across asteroid 101955 Bennu. After mapping the near-Earth asteroid's dark surface, OSIRIS-REx will next touch Bennu's surface in 2020 August to collect a surface sample.  The featured 23-second time-lapse video shows four candidate locations for the touch, from which NASA chose just one earlier this month. NASA chose the Nightingale near Bennu's northern hemisphere as the primary touch-down spot because of its relative flatness, lack of boulders, and apparent abundance of fine-grained sand.  Location Osprey is the backup.  NASA plans to return soil samples for Bennu to Earth in 2023 for a detailed analysis.    Free Presentation: APOD Editor to show best astronomy images of 2019 -- and the decade -- in NYC on January 3",
        'media_type': 'video',
        'service_version': 'v1',
        'title': 'Places for OSIRIS-REx to Touch Asteroid Bennu',
        'url': 'https://www.youtube.com/embed/pvKEG141GmU?rel=0'
    }

    # Obtain given answer
    DATE = datetime.datetime.strptime("2019-12-23", "%Y-%m-%d")
    obtained_info = get_info(DATE)

    assert obtained_info == correct_info
