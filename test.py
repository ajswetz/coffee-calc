from brewratio import *

gLRatio = gramsPerLiterRatio(60)

print(f"grams per liter ratio: {gLRatio}")

print("converting to 'gram coffee per grams water' ratio...")

GperGRatio = gLRatio.convert_to_gram_per_grams()

print(f"gram per grams ratio: {GperGRatio}")

print("converting back to grams per liter...")

gperLRatio = GperGRatio.convert_to_grams_per_liter()

print(f"grams per liter ratio converted: {gperLRatio}")