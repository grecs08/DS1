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
from functions import is_leap_year
# Constants

year = int(input("Enter a year to check if it is a leap year: "))

leap_year = is_leap_year(year)

print(f"{year} is a leap year: {leap_year}")
