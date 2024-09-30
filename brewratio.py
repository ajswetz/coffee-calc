class BrewRatio():
    
    def __repr__(self) -> str:
        pass

class gramsPerLiterRatio(BrewRatio):
    def __init__(self, coffee: int):

        if not isinstance(coffee, (int, float)):
            raise TypeError(f"coffee must be an integer, got {type(coffee).__name__}")
        
        self._coffee = coffee
        self._water_liters = 1
        self._water_mL = 1000

    def __repr__(self):
        return f"{self._coffee} g/L"
    
    def convert_to_gram_per_grams(self):
        grams_water = 1000 / self._coffee
        return gramPerGramsRatio(round(grams_water, 1))
        
class gramPerGramsRatio(BrewRatio):
    def __init__(self, water: int):

        if not isinstance(water, (int, float)):
            raise TypeError(f"water must be an integer, got {type(water).__name__}")
        
        self._coffee = 1
        self._water_grams = water

    def __repr__(self):
        return f"1:{self._water_grams} (1 gram of coffee per {self._water_grams} grams of water)"
        

    def convert_to_grams_per_liter(self):
        grams_coffee = 1000 / self._water_grams
        return gramsPerLiterRatio(round(grams_coffee, 1))
