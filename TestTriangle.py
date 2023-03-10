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
    """ this is the TestTriangle class"""
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        """ this is the testRightTriangleA method"""
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        """ this is the testRightTriangleB method"""
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')

    def testEquilateralTriangleA(self):
        """ this is the testEquilateralTriangleA method"""
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        """ this is the testEquilateralTriangleB method"""
        test_a = 2
        test_b = 2
        test_c = 2
        self.assertEqual(classifyTriangle(test_a,test_b,test_c),'Equilateral','2,2,2 should be equilateral')

    def testIsoscelesTriangleA(self):
        """ this is the testIsoscelesTriangleA method"""
        test_a = 2
        test_b = 2
        test_c = 3
        self.assertEqual(classifyTriangle(test_a,test_b,test_c), 'Isoceles','2,2,3 should be Isoceles')

    def testIsoscelesTriangleB(self):
        """ this is the testIsoscelesTriangleB method"""
        test_a = 1
        test_b = 9
        test_c = 9
        self.assertEqual(classifyTriangle(test_a,test_b,test_c), 'Isoceles','1,9,9 should be Isoceles')

    def testIsoscelesTriangleC(self):
        """ this is the testIsoscelesTriangleC method"""
        test_a = 4
        test_b = 5
        test_c = 4
        self.assertEqual(classifyTriangle(test_a,test_b,test_c), 'Isoceles','4,5,4 should be Isoceles')

    def testScaleneTriangleA(self):
        """ this is the testScaleneTriangleA method"""
        test_a = 9
        test_b = 8
        test_c = 7
        self.assertEqual(classifyTriangle(test_a,test_b,test_c), 'Scalene','9,8,7 should be Scalene')

    def testScaleneTriangleB(self):
        """ this is the testScaleneTriangleB method"""
        test_a = 10
        test_b = 20
        test_c = 30
        self.assertEqual(classifyTriangle(test_a,test_b,test_c), 'Scalene','10,20,30 should be Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
