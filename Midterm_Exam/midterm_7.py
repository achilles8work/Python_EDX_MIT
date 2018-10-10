'''
Problem 7
0.0/20.0 points (graded)
Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)
For your own testing of satisfiesF, for example, see the following test function f and test code:

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
Should print:

2
['a', 'a']
Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.
'''

def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key in d1.keys():
        if key in d2.keys():
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            difference[key] = d2[key]
    return (intersect, difference)
