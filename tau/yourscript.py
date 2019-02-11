import click

# Testing setuptools integration

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')