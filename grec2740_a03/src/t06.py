"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Imports
from functions import reroute
# Constants

opstring = input("Enter opstring: ")

values_in = [1, 2, 3, 4, 5, 6]

values_out = reroute(opstring, values_in)

print(values_out)
