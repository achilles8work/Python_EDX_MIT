'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
'''

#Function to count the no of vowels in the string of lowercase characters
def vowel_count(string):
    vowel_count = 0

    for letter in input_string:
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            vowel_count += 1

    return vowel_count

#Takes string as input and convert it to lowercase if not
input_string = input("Enter the string: ").lower()

count = vowel_count(input_string)

print("Count of Vowels in String: ", count)
