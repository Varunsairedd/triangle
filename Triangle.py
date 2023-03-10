# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    return_response = ''
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return_response = return_response.join('InvalidInput')

    if a <= 0 or b <= 0 or c <= 0:
        return_response = return_response.join('InvalidInput')

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns = True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return_response = return_response.join('InvalidInput')

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if not((a >= (b - c)) or (b >= (a - c)) or (c >= (a + b))):
        return_response = return_response.join('NotATriangle')

    # now we know that we have a valid triangle
    if a == b and b == c and c == a:
        return_response = return_response.join('Equilateral')
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return_response = return_response.join('Right')
    elif (a != b) and  (b != c) and (c != a):
        return_response = return_response.join('Scalene')
    else:
        return_response = return_response.join('Isoceles')
    return return_response
