"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Imports
from functions import clean_list
# Constants


string_values = input('Enter values (seperated by a comma): ').split(',')

values = []

for i in string_values:
    values.append(int(i))

clean_list(values)

print(f'Cleaned List: {values}')
