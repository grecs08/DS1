"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))
