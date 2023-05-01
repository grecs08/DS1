"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
# Constants


stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
