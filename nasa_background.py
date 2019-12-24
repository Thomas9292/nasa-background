import click

from tools import nasa_api, background
from tools.utils import parse_str_to_date


@click.group()
@click.option("--date", default=None, help="Enter the date as a single string in YYYY-MM-DD format.")
@click.pass_context
def nasa_background(ctx, date):
    from datetime import datetime
    if date is None:
        date = datetime.now()
    else:
        date = parse_str_to_date(date)
    ctx.obj = {"DATE": date}


@nasa_background.command()
@click.pass_context
def update(ctx):
    '''Get the newest NASA Picture of the Day and set it as background'''
    try:
        meta_info = nasa_api.get_info(ctx.obj["DATE"])
        click.echo(f"Title: {meta_info['title']}\n")
        click.echo(meta_info['explanation'] + "\n")

        if click.confirm("Do you wish to download this image and set it as background?"):
            file_path = nasa_api.download_image(ctx.obj["DATE"])
            background.change_background(file_path)

    except Exception as e:
        click.echo("Fatal error encountered, exiting program..")
        click.echo(e)


if __name__ == '__main__':
    nasa_background()
