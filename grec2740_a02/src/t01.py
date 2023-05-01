"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-21"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods, by_origin
# Constants


file_variable = open('food.txt', "rt")

foods = read_foods(file_variable)

file_variable.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origin = by_origin(foods, origin)

for food in origin:
    print(food, end="\n\n")
