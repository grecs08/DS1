"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import stack_test
# Constants


file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)
