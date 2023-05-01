"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-02-18"
-------------------------------------------------------
"""
# Imports
from functions import to_power
# Constants

base = float(input("Enter the base value: "))

power = int(input("Enter the power: "))

ans = to_power(base, power)

print(ans)
