"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
# Weight constants
MERCURY = 0.376
VENUS = 0.889
MARS = 0.378
JUPITER = 2.360
SATURN = 1.081
URANUS = 0.815
NEPTUNE = 1.140
EARTH = 1.000


def main():
    # input a weight and a planet
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet (e.g. Mars): ")
    
    # checks which planet constant to use as the gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY
    elif planet == "Venus":
        gravity_constant = VENUS
    elif planet == "Mars":
        gravity_constant = MARS
    elif planet == "Jupiter":
        gravity_constant = JUPITER
    elif planet == "Saturn":
        gravity_constant = SATURN
    elif planet == "Uranus":
        gravity_constant = URANUS
    elif planet == "Neptune":
        gravity_constant = NEPTUNE
    else:
        gravity_constant = EARTH
    
    # convert the weight using the correct gravity constant, then round it
    planet_weight = round(earth_weight * gravity_constant, 2)
    
    print("The equivalent weight on " + planet + ": " + str(planet_weight) )



if __name__ == "__main__":
    main()
