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

@click.command()
@click.option('--brewer',
            type=click.Choice(['v60', 'french-press', 'aeropress'], case_sensitive=False),
            required=True,
            prompt='Which brewer are you using?')
@click.option('--ratio',
            required=False,
            type=float,
            default=60.0)
@click.option('--coffee',
            required=True,
            type=float,
            prompt='How many grams of coffee are you using?')
def recipe(brewer, ratio, coffee):
    click.echo("Executing recipe command . . .")

    water = round(coffee / ratio * 1000)

    match brewer:

        case 'v60':
            click.echo(f'''



            ''')

        case 'french-press':
            click.echo(f'''James Hoffmann French Press Technique:
Source: https://www.youtube.com/watch?v=st571DYYTR8       

Grind Size: Medium
Recommended Ratio: 60-70 g/L
Water Temp: Boiling (100°C / 212°F)
            
Steps:
1. Put {coffee} grams of ground coffee in french press
2. Pour in {water} grams of boiling water
3. Cover gently with the lid, but don't press down the plunger
4. Let sit for 4 minutes
5. Then, remove the lid and stir the crust of coffee grounds
6. Scoop off the foam and floating bits at the top
7. Wait 5-8 more minutes while the grounds sink to the bottom
8. Gently push the plunger down just to the top of the liquid
9. Gently pour the coffee out of the brewer''')

        case 'aeropress':
            click.echo(f'''



            ''')

