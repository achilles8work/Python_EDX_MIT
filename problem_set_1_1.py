'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
'''

#Function to count the no of vowels in the string of lowercase characters
def vowel_count(string):
    vowelCount = 0

    for letter in input_string:
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            vowelCount += 1

    return vowelCount

#Takes string as input and convert it to lowercase if not
inputString = input("Enter the string: ").lower()

count = vowel_count(inputString)

print("Count of Vowels in String: ", count)
