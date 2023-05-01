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
from Stack_array import Stack
from utilities import array_to_stack
# Constants

source1 = Stack()

source2 = Stack()

array_to_stack(source1, [5, 8, 12, 8])

array_to_stack(source2, [3, 6, 1, 7, 9, 14])

target = Stack()

target.combine(source1, source2)

while not target.is_empty():
    value = target.pop()
    print(value)
