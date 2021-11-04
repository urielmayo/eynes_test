import unittest
from main import *
class Test(unittest.TestCase):
    def test_1(self):
        matrix = [
            [2, 3, 4, 5, 1],
            [5, 3, 3, 5, 5],
            [2, 2, 1, 4, 4],
            [5, 1, 3, 4, 3],
            [5, 2, 4, 5, 2]
        ]
        self.assertEqual(
            [((0, 0), (0, 3)), ((4, 4), (4, 1))], 
            get_four_in_line(matrix)
        )
    def test_2(self):
            matrix = [
                [2, 3, 4, 5, 1],
                [5, 3, 3, 5, 5],
                [2, 2, 1, 4, 4],
                [5, 1, 3, 4, 3],
                [5, 2, 4, 5, 2]
            ]
            self.assertEqual(
                [((0, 0), (0, 3)), ((4, 4), (4, 1))], 
                get_four_in_line(matrix)
            )

if __name__=='__main__':
    unittest.main(verbosity=3)