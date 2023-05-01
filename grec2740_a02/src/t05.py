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
from Food_utilities import read_foods, food_table, food_search
# Constants


file_variable = open('food.txt', "rt")

foods = read_foods(file_variable)

file_variable.close()

result = food_search(foods, 7, 0, False)

food_table(result)
