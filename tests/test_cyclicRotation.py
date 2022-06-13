import unittest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from lesson02_arrays import cyclicRotation

class TestIterations(unittest.TestCase):
    def test_example1(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        expectedResult = [9, 7, 6, 3, 8]
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)
   
    def test_example2(self):
        A = [0, 0, 0]
        K = 1
        expectedResult = [0, 0, 0]
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)
    
    def test_example3(self):
        A = [1, 2, 3, 4]
        K = 4
        expectedResult = [1, 2, 3, 4]
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)
    
    def test_emptyArray(self):
        A = []
        K = 3
        expectedResult = []
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)
    
    def test_oneElement(self):
        A = [1]
        K = 3
        expectedResult = [1]
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)
    
    def test_twoElements(self):
        A = [1, 2]
        K = 3
        expectedResult = [2, 1]
        result = cyclicRotation.solution(A, K)
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()