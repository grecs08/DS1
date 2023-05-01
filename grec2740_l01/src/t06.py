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
from Food_utilities import read_food, write_foods
# Constants

pizza = read_food('Pizza|7|False|300')

lasagna = read_food('Lasagna|7|False|135')

file = open("new_foods.txt", "wt")

write_foods(file, [pizza, lasagna])

file.close()
