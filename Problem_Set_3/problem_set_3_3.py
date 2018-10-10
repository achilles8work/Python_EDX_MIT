'''
Problem 3 - Printing Out all Available Letters

Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters - all lowercase English letters
that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
'''
import string

def getAvailableLetters(lettersGuessed):
    alphabets = string.ascii_lowercase
    availableLetters = ''
    for alphabet in alphabets:
        if alphabet not in lettersGuessed:
            availableLetters += alphabet

    return availableLetters
