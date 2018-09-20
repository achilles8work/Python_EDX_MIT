'''
Exercise: guess my number

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
'''


lowerBound = 0
upperBound = 100
char = ''

print('Please think of a number between 0 and 100!')

while char != 'c':
    secretKey = (lowerBound + upperBound)//2
    print('Is your secret number', secretKey, '?')
    choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if choice != 'h' and choice != 'l' and choice != 'c':
        print('Sorry, I did not understand your input.')
    else:
        if choice == 'h':
            upperBound = secretKey
        elif choice == 'l':
            lowerBound = secretKey
        else:
            break

print('Game over. Your secret number was:', secretKey)
