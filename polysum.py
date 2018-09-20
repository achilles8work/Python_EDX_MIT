'''
Grader

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:
The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.
'''
import math

def polysum(n,s):
    area_of_polygon = (0.25 * n * (s**2))/(math.tan(math.pi/n))
    perimeter_of_polygon = s*n
    sum = area_of_polygon + perimeter_of_polygon**2

    return round(sum, 4)
    
