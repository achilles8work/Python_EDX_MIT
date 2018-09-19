'''

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
