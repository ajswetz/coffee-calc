import click

@click.command()
def brew():
    click.echo("Executing brew command . . .")


@click.command()
def convert():
    click.echo("Executing convert command . . .")


