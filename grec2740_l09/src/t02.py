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
from Hash_Set_array import Hash_Set
# Constants

hset = Hash_Set(20)

hset.insert(100)

hset.insert(200)

hset.insert(300)

print("Printing hset: ")
for value in hset:
    print(value)

removed = hset.remove(200)

print()
print("Removed Value: ")
print(removed)

print()
print("Printing hset: ")
for value in hset:
    print(value)
