"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import DATA1, fill_letter_bst, encode_morse
# Constants

bst = BST()

fill_letter_bst(bst, DATA1)

text = input("Enter a String: ")

print(encode_morse(bst, text))
