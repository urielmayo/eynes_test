from main import *
import unittest
class Test(unittest.TestCase):
    def test_1(self):
        example_1 = [
            {'id': 0, 'age': 59}, 
            {'id': 1, 'age': 42}, 
            {'id': 2, 'age': 58}, 
            {'id': 3, 'age': 47}, 
            {'id': 4, 'age': 19}, 
            {'id': 5, 'age': 77}, 
            {'id': 6, 'age': 48}, 
            {'id': 7, 'age': 9}, 
            {'id': 8, 'age': 95},   #oldest person
            {'id': 9, 'age': 5}     #youngest person
        ]

        ordered_list, youngest, oldest = sort_ids_list(example_1)

        self.assertEqual(9, youngest)   #id of youngest person
        self.assertEqual(8, oldest)     #id of oldest person

    def test_2(self):
        example_2 = [
            {'id': 0, 'age': 43}, 
            {'id': 1, 'age': 39}, 
            {'id': 2, 'age': 38}, 
            {'id': 3, 'age': 48}, 
            {'id': 4, 'age': 10}, 
            {'id': 5, 'age': 71},   #oldest person
            {'id': 6, 'age': 5},    #youngest person
            {'id': 7, 'age': 12}, 
            {'id': 8, 'age': 62}, 
            {'id': 9, 'age': 35}
        ]

        ordered_list, youngest, oldest = sort_ids_list(example_2)

        self.assertEqual(6, youngest)   #id of youngest person
        self.assertEqual(5, oldest)     #id of oldest person


if __name__=='__main__':
    unittest.main(verbosity=5)