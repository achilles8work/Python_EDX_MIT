'''
Problem 2 - Printing Out the User's Guess

Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord,
and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores,
based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
'''
def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = ''
    for char in secretWord:
        if char in lettersGuessed:
            guessedWord += char
        else:
            guessedWord += '_ '

    return guessedWord
