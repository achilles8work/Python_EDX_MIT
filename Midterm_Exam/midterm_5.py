'''
Problem 5
0.0/20.0 points (graded)
Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)
'''

def dotProduct(listA, listB):
    sum = 0
    for i in range(len(listA)):
        sum += listA[i]*listB[i]
    return sum
