import click

from tools import nasa_api, background
from tools.utils import parse_str_to_date


@click.group()
def nasa_background():
    pass


@nasa_background.command()
@click.option("--date",
              default=None,
              help="Enter the date as a single string in YYYYMMDD or YYYY-MM-DD format." )
@click.option("--auto",
              is_flag=True,
              help="Disables prompts and sets the background automatically if this can succefully be completed.s" )
def update(date, auto):
    '''Get the newest NASA Picture of the Day and set it as background'''
    # Check if date is passed as argument, set to default (today) otherwise
    if date is None:
        date = datetime.now()
    else:
        date = parse_str_to_date(date)

    try:
        # Download and print information about
        meta_info = nasa_api.get_info(date)
        click.echo(f"Title: {meta_info['title']}\n")
        click.echo(meta_info['explanation'] + "\n")

        # Check if auto is selected, otherwise prompt user to set it as background
        if auto or click.confirm("Do you wish to download this image and set it as background?"):
            # Download and set the background
            file_path = nasa_api.download_image(date)
            background.change_background(file_path, auto)
    except KeyError:
        click.echo(f"Image not found for the selected date {date}. ")
    except Exception as e:
        click.echo("Fatal error encountered, exiting program.")
        click.echo(e)


if __name__ == '__main__':
    nasa_background()
