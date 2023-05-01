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
from Food_utilities import read_food
# Constants

line = input(
    "Enter food details in the format (name|origin|is_vegetarian|calories): ")

food = read_food(line)

print(food)
