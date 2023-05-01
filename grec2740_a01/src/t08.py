"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-13"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants


a = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
small, large, total, average = matrix_stats(a)

print(f"{small}, {large}, {total}, {average}")
