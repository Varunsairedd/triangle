# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        a = 2
        b = 2
        c = 2
        self.assertEqual(classifyTriangle(a,b,c),'Equilateral','2,2,2 should be equilateral')

    def testIsoscelesTriangleA(self):
        a = 2
        b = 2
        c = 3
        self.assertEqual(classifyTriangle(a,b,c), 'Isoceles','2,2,3 should be Isoceles')
    
    def testIsoscelesTriangleB(self):
        a = 1
        b = 9
        c = 9
        self.assertEqual(classifyTriangle(a,b,c), 'Isoceles','1,9,9 should be Isoceles')

    def testIsoscelesTriangleC(self):
        a = 4
        b = 5
        c = 4
        self.assertEqual(classifyTriangle(a,b,c), 'Isoceles','4,5,4 should be Isoceles')

    def testScaleneTriangleA(self):
        a = 9
        b = 8
        c = 7
        self.assertEqual(classifyTriangle(a,b,c), 'Scalene','9,8,7 should be Scalene')

    def testScaleneTriangleB(self):
        a = 10
        b = 20
        c = 30
        self.assertEqual(classifyTriangle(a,b,c), 'Scalene','10,20,30 should be Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
