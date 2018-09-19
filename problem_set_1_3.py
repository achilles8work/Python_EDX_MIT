'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
#function to identify the longest substring in alphabetical order
def longest_alphabet(string):
    count = 0
    maxlen = 0
    result = 0

    for index in range(len(string)-1):
        #increase the count when condition is true i.e substring is in alphabetical order,
        #if condition fails counter is set to 0
        if string[index] < string[index+1]:
            count += 1

            if count > maxlen:
                maxlen = count
                result = index + 1
        else:
            count = 0

    startPosition = result - maxlen
    return string[startPosition:result+1]

inputString = input("Enter the String: ").lower()

longestSubstring = longest_alphabet(inputString)

print("Longest substring in alphabetical order:",longestSubstring)
