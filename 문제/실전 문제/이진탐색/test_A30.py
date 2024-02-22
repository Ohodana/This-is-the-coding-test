import unittest

from A30 import solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        # Test case 1
        n = 5
        c = 3
        houses = [1, 2, 8, 4, 9]
        self.assertEqual(solution(n, c, houses), 3)

        # Test case 2
        n = 6
        c = 2
        houses = [1, 3, 5, 7, 9, 11]
        self.assertEqual(solution(n, c, houses), 5)

        # Test case 3
        n = 7
        c = 4
        houses = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual(solution(n, c, houses), 4)

if __name__ == '__main__':
    unittest.main()