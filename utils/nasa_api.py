import os
from datetime import datetime

import click
import requests

IMAGE_FOLDER = os.path.join(os.path.expanduser('~/Pictures'), 'NASA')
URL = 'https://api.nasa.gov/'
POD_ENDPOINT = 'planetary/apod'
API_KEY = 'DEMO_KEY'

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

def get_info(date=datetime.today()):
    """
    Downloads the meta-info about the picture of the day for specified date

    Arguments:
    date -- date for which POD should be retrieved, defaults to today

    Output:
    Dictionary with meta-information about POD
    """
    try:
        params = {
            'date': date.strftime("%Y-%m-%d"),
            'hd': True,
            'api_key': API_KEY
        }

        response = requests.get(URL + POD_ENDPOINT, params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        click.echo(e)
        click.echo(f"Could not download meta-info for POD {date.date()}..")
        raise e


def download_image(date=datetime.today()):
    """
    Downloads the hd image for a specified date, and shows progress bar

    Arguments:
    date -- date for which POD should be retrieved, defaults to today
    """
    try:
        meta_info = get_info(date=date)
        url = meta_info['hdurl']

        title = meta_info['title'].replace(' ', '_')
        img_name = f"{date.strftime('%Y-%m-%d')}_{title}.jpg"
        img_path = os.path.join(IMAGE_FOLDER, img_name)

        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length'))

        with open(img_path, 'wb') as local_file:
            with click.progressbar(
                    length=total_size, label=f"Downloading - {meta_info['title']} ({date.date()})") as bar:
                for data in response.iter_content(chunk_size=4096):
                    local_file.write(data)
                    bar.update(len(data))
    except Exception as e:
        click.echo("Could not download")
        raise e
