import click
import re
from brewratio import *

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
@click.option('--from', 'from_',
        required=True,
        prompt='Enter the ratio you want to convert FROM. Accepted input examples: "60"; "1:15"')
def convert(from_):
    click.echo("Executing convert command . . .")

    match = re.search(r"(\d{2})|(\d:\d{2}\.?\d?)", from_)
    if not match:
        raise ValueError(f"Your input ratio '{from_}' is invalid. Accepted input examples: '60'; '70'; '1:15'; '1:16.5'")
    
    #Else - must be a valid ratio - continue with script
    
    input_ratio = match.group()
    
    if ':' in input_ratio:
        grams_water = float(input_ratio.split(':')[1])
        click.echo(f"Your input ratio is: {input_ratio}")
        given_ratio = gramPerGramsRatio(grams_water)
        click.echo(f"Your new ratio is: {given_ratio.convert_to_grams_per_liter()}")


    else:
        grams_coffee = float(input_ratio)
        click.echo(f"Your input ratio is: {grams_coffee} g/L")
        given_ratio = gramsPerLiterRatio(grams_coffee)
        click.echo(f"Your new ratio is: {given_ratio.convert_to_gram_per_grams()}")





