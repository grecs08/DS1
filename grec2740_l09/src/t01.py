"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_food
from functions import hash_table
# Constants

food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])
