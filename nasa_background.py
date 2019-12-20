import click

from utils import nasa_api, background


@click.group()
def nasa_background():
    pass

@nasa_background.command()
def update():
    '''Get the newest NASA Picture of the Day and set it as background'''
    try:
        meta_info = nasa_api.get_info()
        click.echo(f"Title: {meta_info['title']}\n")
        click.echo(meta_info['explanation'] + "\n")

        if click.confirm("Do you wish to download this image and set it as background?"):
            file_path = nasa_api.download_image()
            background.change_background(file_path)

    except Exception as e:
        click.echo("Fatal error encountered, exiting program..")
        click.echo(e)


if __name__ == '__main__':
    nasa_background()
