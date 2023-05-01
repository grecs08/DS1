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
from List_array import List
# Constants

list1 = List()

list1.append(100)

print(len(list1))

list1.insert(0, 200)

print(len(list1))

remove = list1.remove(200)

print(remove)
