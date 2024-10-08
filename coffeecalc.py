import click
import re
from brewratio import *

@click.command()
@click.option('--with', 'with_',
            type=click.Choice(['coffee', 'water'], case_sensitive=False),
            required=True,
            prompt='Start your calculation with a value for either coffee or water',
            help="Whether coffee or water should serve as the starting point for your calculation.")
@click.option('--grams',
            required=True,
            type=float,
            prompt='Enter your starting amount of coffee OR water in grams',
            help="Starting amount of coffee OR water in grams. For water, 1g = 1mL.")
@click.option('--ratio',
            required=False,
            type=float,
            default=60.0,
            help="Your desired ratio of coffee-to-water. If not specified, the default ratio of 60 g/L will be used.")
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
        prompt='Enter the ratio you want to convert FROM. Accepted input examples: "60"; "1:15"',
        help="The ratio you want to convert FROM. To convert from a ratio like '60 g/L', the valid input would just be '60'. To convert from a ratio like '1:15', the valid input would be '1:15'.")
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
            prompt='Which brewer are you using?',
            help="The coffee brewer you're using.")
@click.option('--ratio',
            required=False,
            type=float,
            default=60.0,
            help="Your desired ratio of coffee-to-water. If not specified, the default ratio of 60 g/L will be used.")
@click.option('--coffee',
            required=True,
            type=float,
            prompt='How many grams of coffee are you using?',
            help="The amount of grams of coffee you're using.")
def recipe(brewer, ratio, coffee):
    click.echo("Executing recipe command . . .")

    water = round(coffee / ratio * 1000)

    match brewer:

        case 'v60':
            click.echo(f'''James Hoffmann V60 Technique:
Source: https://www.youtube.com/watch?v=AI4ynXzkSQo
                       
Grind Size: Medium Fine
Recommended Ratio: 60 g/L
Water Temp: 
    Lighter roasts: Boiling (100°C / 212°F)
    Darker roasts: 80-90°C / 176-194°F

Steps:
1. Rinse paper filter with water just off the boil
2. Add ground coffee to the V60
3. Create a well in the middle of the grounds to help saturation during the bloom
4. Zero out the scale and start the timer
5. Bloom: Add 2x-3x coffee weight in water ({round(coffee * 2)}-{round(coffee * 3)} grams)
6. Swirl or stir the coffee slurry until evenly mixed
7. Wait until 0:45 seconds on the timer
8. At 0:45 seconds, pour water up to a total of {round(water * .6)} grams within the next 30 seconds
9. At 1:15 seconds, pour water up to a total of {water} grams within the next 30 seconds
10. Then, gently stir the top of the slurry with a spoon to knock off grounds from the side of the brewer
11. Allow the V60 to drain a little
12. Give the V60 a gentle swirl (helps achieve flat coffee bed for even extraction)
13. Allow the water to finish draining through the coffee bed
14. Aim to finish drawdown by approximately 3:30 (this can vary based on total volume of coffee brewed)
15. Enjoy!''')

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
9. Gently pour the coffee out of the brewer
10. Enjoy!''')

        case 'aeropress':
            if coffee > 18:
                click.secho("===============================================================================", fg="red")
                click.secho("WARNING: THIS RECIPE WILL NOT WORK WITH MORE THAN 18G OF COFFEE!", fg="red")
                click.secho("IF YOU WANT TO BREW A LARGER BATCH WITH YOUR AEROPRESS, USE A DIFFERENT RECIPE.", fg="red")
                click.secho("HERE'S ONE SUGGESTION: https://aeroprecipe.com/recipes/backpack-of-freedom", fg="red")
                click.secho("===============================================================================", fg="red")
            else: 

                click.echo(f'''James Hoffmann Aeropress Technique
Source: https://www.youtube.com/watch?v=XGs5QVAU-00
                       
Grind Size: Finer end of medium
Recommended Ratio: 55 g/L
Water Temp: 
    Light roasts: 99°C / 210°F
    Medium roasts: 90-95°C / 194-203°F
    Dark roasts: 85-90°C / 185-194°F

Steps:
1. Set brewer with filter in standard position on a server or cup.
2. Don't rinse the paper filter or preheat the brewer.
3. Add {coffee} grams of coffee to the Aeropress.
3. Start a timer, add {water} grams of water, aiming to wet all the coffee.
4. Immediately place the plunger on top of the brewer (about 1cm in) to stop the coffee from dripping.
5. Wait 2 minutes.
6. Holding the brewer and the plunger, gently swirl the brewer.
7. Wait 30 seconds.
8. Gently press all the way down. It will take about 30 seconds.
9. Enjoy!''')