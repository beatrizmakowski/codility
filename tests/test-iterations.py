import unittest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from lesson01_iterations import iterations

class TestIterations(unittest.TestCase):
    def test_9(self):
        result = iterations.solution(9)
        self.assertEqual(result, 2)
    
    def test_529(self):
        result = iterations.solution(529)
        self.assertEqual(result, 4)

    def test_20(self):
        result = iterations.solution(20)
        self.assertEqual(result, 1)
    
    def test_15(self):
        result = iterations.solution(15)
        self.assertEqual(result, 0)

    def test_32(self):
        result = iterations.solution(32)
        self.assertEqual(result, 0)

    def test_1041(self):
        result = iterations.solution(1041)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()