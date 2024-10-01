import click

@click.command()
@click.option('--with', 'with_',
            type=click.Choice(['coffee', 'water'], case_sensitive=False),
            required=True,
            prompt='Start your calculation with a value for either coffee or water')
@click.option('--grams',
            required=True,
            type=float,
            prompt='Enter your starting amount of coffee OR water in grams')
@click.option('--ratio',
            required=False,
            type=float,
            default=60.0)
def brew(with_, grams, ratio):
    click.echo("Executing brew command . . .")
    click.echo(f"Your brew ratio is: {ratio} g/L")
    match with_.lower():
        case 'coffee':
            water = round(grams / ratio * 1000)
            click.echo(f"Starting with {grams} grams of ground coffee, you will need to use {water} grams of water.")
        case 'water':
            coffee = round(grams / 1000 * ratio, 1)
            click.echo(f"To make {grams} grams of brewed coffee, you will need to use {coffee} grams of ground coffee.")


@click.command()
def convert():
    click.echo("Executing convert command . . .")


