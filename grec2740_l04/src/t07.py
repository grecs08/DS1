"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test
# Constants

file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)
