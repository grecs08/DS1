"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-15"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, get_vegetarian
# Constants

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")
