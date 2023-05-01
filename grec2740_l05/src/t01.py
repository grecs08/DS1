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
from functions import recurse
# Constants

x = int(input("Enter a value: "))

y = int(input("Enter another value: "))

ans = recurse(x, y)

print(ans)
