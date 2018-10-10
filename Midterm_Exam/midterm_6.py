'''
Problem 6
0.0/20.0 points (graded)
Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces together two strings. Your procedure should not use any explicit loop mechanism, such as a for or while loop. We have provided a template of the code; your job is to insert a single line of code in each of the indicated places.

For this problem, you must add exactly one line of code in each of the three places where we specify to write a line of code. If you add more lines, your code will not count as correct.
'''

def deep_reverse(L):
    result = []
    for i in L:
        result.append(i[::-1])
    L[:] = result[::-1]
    return L

