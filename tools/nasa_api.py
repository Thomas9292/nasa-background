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
        click.echo(f"Could not download meta-info for POD {date.date()}..")
        raise e


def download_image(date=datetime.today()):
    """
    Downloads the hd image for a specified date, and shows progress bar

    Arguments:
    date -- date for which POD should be retrieved, defaults to today

    Output:
    File path of saved image
    """
    try:
        # Download meta_info for url
        meta_info = get_info(date=date)
        print(meta_info.keys())
        if "hdurl" not in meta_info.keys():
            raise KeyError("download_image: meta_info does not contain hdurl.")
        url = meta_info['hdurl']

        # Construct path to save image
        title = meta_info['title'].replace(' ', '-')
        img_name = f"{date.strftime('%Y-%m-%d')}_{title}.jpg"
        img_path = os.path.join(IMAGE_FOLDER, img_name)

        # Check if img is already downloaded
        if os.path.exists(img_path):
            click.echo(
                "Today's image has already been downloaded and is now being set as background."
            )

        else:
            # Initialize stream and filesize
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length'))

            with open(img_path, 'wb') as local_file:
                # Initialize progress bar
                with click.progressbar(
                        length=total_size,
                        label=
                        f"Downloading - {meta_info['title']} ({date.date()})"
                ) as bar:
                    # Download chunks and update progress bar
                    for data in response.iter_content(chunk_size=4096):
                        local_file.write(data)
                        bar.update(len(data))

        return img_path

    except KeyError as e:
        raise e
    except Exception as e:
        click.echo(f"Could not download: {meta_info['title']}")
        raise e
