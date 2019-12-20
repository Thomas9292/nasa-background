import click

@click.group()
def nasa_background():
    pass

@nasa_background.command()
def cmd1():
    '''Command on nasa_background'''
    click.echo('nasa_background cmd1')

@nasa_background.command()
def cmd2():
    '''Command on nasa_background'''
    click.echo('nasa_background cmd2')

if __name__ == '__main__':
    nasa_background()
