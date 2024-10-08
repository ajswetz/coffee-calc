# Coffee Calc

## Overview
Brewing coffee is a science. The key to a delicious cup **every day** is a little math. This calculator does the math for you so you can make amazing coffee with little effort. Let Coffee Calc handle the numbers. You enjoy the brew.

## Getting Started
First, you need to have Python 3 installed on your computer. If you need guidance with this step, check out this guide: [Python For Beginners](https://www.python.org/about/gettingstarted/).

Second, for simple installation, I recommend you install `Git`. If you need guidance with this step, check out this guide: [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Third, run these commands to clone the Coffee Calc repository:

```
git clone https://github.com/ajswetz/coffee-calc
cd coffee-calc
```

### Installing Coffee Calc in a Python Virtual Environment
I recommend installing Coffee Calc in a virtual environment to avoid conflicts with system-wide dependencies. Here are the steps:

1. Create a virtual environment

    `python3 -m venv venv`

2. Activate the virtual environment:

    * On Linux / MacOS:
    
        `source venv/bin/activate`

    * On Windows:

        `venv\Scripts\activate`

3. Install Coffee Calc using `pip`:

    `pip install .`

**NOTE:** You will need to enable the virtual environment using the same command mentioned above each time you want to use the Coffee Calc app. To exit the virtual environment, simply enter the command `deactivate` from the terminal with the virtual environment activated.

## Using Coffee Calc
Coffee Calc currently has three commands: `brew`, `convert`, and `recipe`. Keep reading for usage instructions and examples for each command.

### Brew
The `brew` command is used to calculate the specific amount of coffee and water you need to use based on a given brew ratio. You can specify a ratio if desired, or let Coffee Calc use the default recommended brew ratio (60 grams of coffee per liter of water).

You also need to specify whether to use `water` or `coffee` as the starting point for the calculation.

#### Examples:

1. Calculate amount of water required to brew 30 grams of coffee using default ratio:
```
$ brew --with coffee --grams 30

Executing brew command . . .
Your brew ratio is: 60.0 g/L
Starting with 30.0 grams of ground coffee, you will need to use 500 grams of water.
```


2. Calculate amount of water required to brew 30 grams of coffee using a ratio of 55 g/L. 
```
$ brew --with coffee --grams 30 --ratio 55

Executing brew command . . .
Your brew ratio is: 55.0 g/L
Starting with 30.0 grams of ground coffee, you will need to use 545 grams of water.
```


3. Calculate amount of coffee required to brew with 750 grams (=750 mL) of water using default ratio:
```
$ brew --with water --grams 750

Executing brew command . . .
Your brew ratio is: 60.0 g/L
To make 750.0 grams of brewed coffee, you will need to use 45.0 grams of ground coffee.
```


4. Calculate amount of coffee required to brew with 500 grams (=500 mL) of water using a ratio of 65 g/L.
```
$ brew --with water --grams 500 --ratio 65

Executing brew command . . .
Your brew ratio is: 65.0 g/L
To make 500.0 grams of brewed coffee, you will need to use 32.5 grams of ground coffee.
```

### Convert
The `convert` command is used to convert between the two most common formats of coffee brewing ratios:

* Grams of coffee per liter of water (usually written like this: 60 g/L)
* Grams of water per 1 gram of coffee (usually written like this: 1:15)

#### Examples:

1. Convert *from* 60 g/L to the "grams of water per 1 gram of coffee" format:
```
$ convert --from 60

Executing convert command . . .
Your input ratio is: 60.0 g/L
Your new ratio is: 1:16.7 (1 gram of coffee per 16.7 grams of water)
```

2. Convert *from* 1:15 to the "grams of coffee per liter" format:
```
$ convert --from 1:15

Executing convert command . . .
Your input ratio is: 1:15
Your new ratio is: 66.7 g/L
```


### Recipe
The `recipe` command is used to display popular coffee brewing recipes based on the coffee brewer you'll be using. The current options available are: v60, french press, and Aeropress.

This command will also customize the recipe to include your desired amount of coffee and brew ratio. If no ratio is specified, the default ratio of 60 g/L will be used.

#### Examples:

1. Get a recipe for brewing with the Hario V60 using 45g coffee:

```
$ recipe --brewer v60 --ratio 60 --coffee 45

Executing recipe command . . .
James Hoffmann V60 Technique:
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
5. Bloom: Add 2x-3x coffee weight in water (90-135 grams)
6. Swirl or stir the coffee slurry until evenly mixed
7. Wait until 0:45 seconds on the timer
8. At 0:45 seconds, pour water up to a total of 450 grams within the next 30 seconds
9. At 1:15 seconds, pour water up to a total of 750 grams within the next 30 seconds
10. Then, gently stir the top of the slurry with a spoon to knock off grounds from the side of the brewer
11. Allow the V60 to drain a little
12. Give the V60 a gentle swirl (helps achieve flat coffee bed for even extraction)
13. Allow the water to finish draining through the coffee bed
14. Aim to finish drawdown by approximately 3:30 (this can vary based on total volume of coffee brewed)
15. Enjoy!
```

2. Get a recipe for brewing with a french press using 60g coffee:
```
$ recipe --brewer french-press --ratio 60 --coffee 60
Executing recipe command . . .
James Hoffmann French Press Technique:
Source: https://www.youtube.com/watch?v=st571DYYTR8

Grind Size: Medium
Recommended Ratio: 60-70 g/L
Water Temp: Boiling (100°C / 212°F)

Steps:
1. Put 60.0 grams of ground coffee in french press
2. Pour in 1000 grams of boiling water
3. Cover gently with the lid, but don't press down the plunger
4. Let sit for 4 minutes
5. Then, remove the lid and stir the crust of coffee grounds
6. Scoop off the foam and floating bits at the top
7. Wait 5-8 more minutes while the grounds sink to the bottom
8. Gently push the plunger down just to the top of the liquid
9. Gently pour the coffee out of the brewer
10. Enjoy!
```

3. Get a recipe for brewing with the Aeropress using 15g coffee:
```
$ recipe --brewer aeropress --ratio 60 --coffee 15
Executing recipe command . . .
James Hoffmann Aeropress Technique
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
3. Add 15.0 grams of coffee to the Aeropress.
3. Start a timer, add 250 grams of water, aiming to wet all the coffee.
4. Immediately place the plunger on top of the brewer (about 1cm in) to stop the coffee from dripping.
5. Wait 2 minutes.
6. Holding the brewer and the plunger, gently swirl the brewer.
7. Wait 30 seconds.
8. Gently press all the way down. It will take about 30 seconds.
9. Enjoy!
```

## Getting help within the app

You can use the `--help` option with any of the Coffee Calc commands to see basic help information within your terminal.

### Examples:

```
$ brew --help
Usage: brew [OPTIONS]

Options:
  --with [coffee|water]  Whether coffee or water should serve as the starting
                         point for your calculation.  [required]
  --grams FLOAT          Starting amount of coffee OR water in grams. For
                         water, 1g = 1mL.  [required]
  --ratio FLOAT          Your desired ratio of coffee-to-water. If not
                         specified, the default ratio of 60 g/L will be used.
  --help                 Show this message and exit.
```

```
$ convert --help
Usage: convert [OPTIONS]

Options:
  --from TEXT  The ratio you want to convert FROM. To convert from a ratio
               like '60 g/L', the valid input would just be '60'. To convert
               from a ratio like '1:15', the valid input would be '1:15'.
               [required]
  --help       Show this message and exit.
```

```
$ recipe --help
Usage: recipe [OPTIONS]

Options:
  --brewer [v60|french-press|aeropress]
                                  The coffee brewer you're using.  [required]
  --ratio FLOAT                   Your desired ratio of coffee-to-water. If
                                  not specified, the default ratio of 60 g/L
                                  will be used.
  --coffee FLOAT                  The amount of grams of coffee you're using.
                                  [required]
  --help                          Show this message and exit.
```