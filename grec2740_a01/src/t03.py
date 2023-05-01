"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-11"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

filename = "fv"
testing_file = open(filename, "r", encoding="utf-8")

u, l, d, w, r = file_analyze(testing_file)
print(f"There are {u} uppercase letters in the file")
print(f"There are {l} lowercase letters in the file")
print(f"There are {d} digits in the file")
print(f"There are {w} white spaces in the file")
print(f"There are {r} remaining characters in the file")

testing_file.close()
