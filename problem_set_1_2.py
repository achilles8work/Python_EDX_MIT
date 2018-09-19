'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example,
if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
#function to count the string 'bob' in the input string
def count_bob(string):

    count = 0

    for index in range(len(string) - 1):
        #slice the string from current index position till last and check whether string starts with bob
        if string[index:].startswith('bob'):
            count += 1

    return count

inputString = input("Enter the string: ").lower()

bobCount = count_bob(inputString)

print("Count of bob in input string:",bobCount)
