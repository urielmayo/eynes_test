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
            {((4, 4), (4, 1)), ((0, 0), (0, 3))}, 
            get_four_in_line(matrix)
        )
    def test_2(self):
            matrix = [
                [2, 3, 3, 5, 1],
                [5, 2, 3, 5, 5],
                [2, 3, 4, 5, 4],
                [5, 4, 3, 4, 3],
                [5, 5, 4, 5, 2]
            ]
            self.assertEqual(
                {((2, 0), (2, 3)), ((1, 1), (1, 4)), ((4,4),(4,1))},
                get_four_in_line(matrix)
            )
    def test_3(self):
            matrix = [
                [2, 3, 3, 5, 1],
                [5, 2, 3, 5, 5],
                [1, 3, 4, 5, 1],
                [5, 1, 3, 4, 3],
                [5, 5, 4, 5, 2]
            ]
            self.assertEqual(
                set(),
                get_four_in_line(matrix)
            )

if __name__=='__main__':
    unittest.main(verbosity=2)