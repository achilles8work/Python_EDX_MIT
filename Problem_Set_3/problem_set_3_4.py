'''
Problem 4 - The Game

Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess.
This starts up an interactive game of Hangman between the user and the computer.
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py)
to load the words and pick a random one. Note that the functions loadWords and chooseWord
should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor,
you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter,
the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters,
you should print a message telling them they've already guessed that - so try again!).
'''

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinkng of a word that is", str(len(secretWord)), "letters long")
    print("-----------")
    guessLeft = 8
    lettersGuessed = []
    while guessLeft > 0 and not isWordGuessed(secretWord,lettersGuessed):
        print("You have", guessLeft, "guesses left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            else:
                guessLeft -= 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
        else:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))

        print("-----------")

    if isWordGuessed(secretWord,lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord)
