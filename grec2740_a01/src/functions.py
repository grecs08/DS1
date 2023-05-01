"""
-------------------------------------------------------
[Assignment 1]
-------------------------------------------------------
Author:  Andrew Greco
ID:      210422740
Email:   grec2740@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Imports

# Constants
VOWELS = ['a', 'e', 'i', 'o', 'u']


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_list = []
    index = 0
    while index < len(values):
        if values[index] not in temp_list:
            temp_list.append(values[index])
        else:
            values.pop(index)
            index -= 1
        index += 1
    return


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    remove_a = s.replace("a", "")
    remove_e = remove_a.replace("e", "")
    remove_i = remove_e.replace("i", "")
    remove_o = remove_i.replace("o", "")
    remove_u = remove_o.replace("u", "")
    out = remove_u
    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u, l, d, w, r = 0, 0, 0, 0, 0
    for i in fv.read():
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i == " ":
            w += 1
        else:
            r += 1
    return u, l, d, w, r


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = False

    s = s.lower()

    if s == s[::-1]:
        palindrome = True
        return palindrome
    else:
        return palindrome


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    greatest = 0
    least = 0

    for i in range(len(a)):
        if a[i] - a[i - 1] <= least:
            least = a[i]
        elif a[i] >= greatest:
            greatest = a[i]
    md = greatest - least
    return md


def matrix_transpose(a, b):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    for i in range(len(a[0])):
        row = []
        for item in a:
            row.append(item[i])
        b.append(row)
    return b


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    average = 0
    for lists in a:
        for value in lists:
            if value < small:
                small = value
            elif value > large:
                large = value
            total += value
            average += 1
    average = total / average
    return small, large, total, average


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    if word[0].lower() in VOWELS:
        pl = word + 'way'
    else:
        capital = False
        index = 0
        not_done = True
        temp_word = ""
        if word[0].isupper():
            capital = True
        while index < len(word) and not_done:
            if word[index] in VOWELS:
                not_done = False
            else:
                temp_word += word[index].lower()
                index += 1
        pl = word[index:] + temp_word + 'ay'
        if capital:
            pl = pl.capitalize()
    return pl
