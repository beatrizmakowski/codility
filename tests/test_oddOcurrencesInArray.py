from random import random
import unittest
import sys, os
import random
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from lesson02_arrays import oddOccurrencesInArray


MAX_VALUE = 1000000

def generateRandomArray(size, unmatchedElement):
    randomArray = []
    for _ in range(int((size - 1) / 2)):
        randomValue = random.randint(1, MAX_VALUE)
        for _ in range(2):
            randomArray.append(randomValue)
    randomArray.append(unmatchedElement)
    random.shuffle(randomArray)
    return randomArray


class TestIterations(unittest.TestCase):
    def test_example1(self):
        A = [9, 3, 9, 3, 9, 7, 9]
        expectedResult = 7
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_simple1(self):
        A = generateRandomArray(5, 4)
        expectedResult = 4
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_simple2(self):
        A = generateRandomArray(11, 7)
        expectedResult = 7
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_extreme_single_item(self):
        A = [42]
        expectedResult = 42
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_small1(self):
        A = generateRandomArray(201, 42)
        expectedResult = 42
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_small2(self):
        A = generateRandomArray(601, 43)
        expectedResult = 43
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_medium1(self):
        A = generateRandomArray(2001, 44)
        expectedResult = 44
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_medium2(self):
        A = generateRandomArray(100003, 500000)
        expectedResult = 500000
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)
    
    def test_big1(self):
        A = generateRandomArray(999999, 700)
        expectedResult = 700
        result = oddOccurrencesInArray.solution(A)
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()