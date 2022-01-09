import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')

import unittest

from src.utils import flatten, get_indexes_of, collapse, distribute, tuple_flatten

class Test_flatten(unittest.TestCase):

    def test1(self):
        input = []
        res = flatten(input)
        expected = []
        self.assertEqual(expected, res)

    def test2(self):
        input = [1, 2, 3, 4]
        res = flatten(input)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, res)

    def test3(self):
        input = [[1, 2], [[3, 4]]]
        res = flatten(input)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, res)

    def test4(self):
        input = [1, [2, 3, 4]]
        res = flatten(input)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, res)

    def test5(self):
        input = [[[[1, 2, 3, 4]]]]
        res = flatten(input)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, res)

class Test_tuple_flatten(unittest.TestCase):

    def test1(self):
        input = []
        res = tuple_flatten(input)
        expected = []
        self.assertEqual(expected, res)

    def test2(self):
        input = [1, 2, 3, 4]
        res = tuple_flatten(input)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, res)

    def test3(self):
        input = ()
        res = tuple_flatten(input)
        expected = ()
        self.assertEqual(expected, res)

    def test4(self):
        input = (1, 2, 3, 4)
        res = tuple_flatten(input)
        expected = (1, 2, 3, 4)
        self.assertEqual(expected, res)

    def test5(self):
        input = 2
        res = tuple_flatten(input)
        expected = 2
        self.assertEqual(expected, res)

    def test6(self):
        input = [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
        res = tuple_flatten(input)
        expected = [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
        self.assertEqual(expected, res)

    def test7(self):
        input = [(1, 2, 3), 2, [(1, 2, 3)]]
        res = tuple_flatten(input)
        expected = [(1, 2, 3), 2, [(1, 2, 3)]]
        self.assertEqual(expected, res)

    def test8(self):
        input = [((1, 2, 3), 2), (1, 2, 3), (1, 2, (1, 2, (1, 2, 3)))]
        res = tuple_flatten(input)
        expected = [(1, 2, 3, 2), (1, 2, 3), (1, 2, 1, 2, 1, 2, 3)]
        self.assertEqual(expected, res)

    def test9(self):
        input = ([1, 2, 3], [1, 2], [3])
        res = tuple_flatten(input)
        expected = ([1, 2, 3], [1, 2], [3])
        self.assertEqual(expected, res)

class Test_get_indexes_of(unittest.TestCase):

    def test1(self):
        input = []
        res = get_indexes_of(3, input)
        expected = []
        self.assertEqual(expected, res)

    def test2(self):
        input = [1, 2, 3, 4]
        res = get_indexes_of(3, input)
        expected = [2]
        self.assertEqual(expected, res)

    def test3(self):
        input = [3, 3, 4, 3]
        res = get_indexes_of(3, input)
        expected = [0, 1, 3]
        self.assertEqual(expected, res)
class Test_collapse(unittest.TestCase):

    def test1(self):
        structure = 'd4'
        res = collapse(structure)
        expected = 'd4'
        self.assertEqual(res, expected)

    def test2(self):
        structure = ('d4')
        res = collapse(structure)
        expected = ('d4')
        self.assertEqual(res, expected)

    def test3(self):
        structure = ['d4', 'd5', 'd6']
        res = collapse(structure)
        expected = ['d4', 'd5', 'd6']
        self.assertEqual(res, expected)

    def test4(self):
        structure = ('w2', ['d4', 'd5', 'd6'])
        res = collapse(structure)
        expected = [('w2', 'd4'), ('w2', 'd5'), ('w2', 'd6')]
        self.assertEqual(res, expected)

    def test5(self):
        structure = [('w1', ['d1', 'd2', 'd3']), ('w2', ['d4', 'd5', 'd6']), ('w3', ['d7', 'd8', 'd9'])]
        res = collapse(structure)
        expected = [('w1', 'd1'), ('w1', 'd2'), ('w1', 'd3'), ('w2', 'd4'), ('w2', 'd5'), ('w2', 'd6'), ('w3', 'd7'), ('w3', 'd8'), ('w3', 'd9')]
        self.assertEqual(res, expected)

    def test6(self):
        structure = [
            ('f1', [('w1', ['d1', 'd2', 'd3']), ('w2', ['d4', 'd5', 'd6']), ('w3', ['d7', 'd8', 'd9'])]),
            ('f2', [('w4', ['d10', 'd11', 'd12']), ('w5', ['d13', 'd14', 'd15'])]),
            ('f3', [('w6', ['d16', 'd17', 'd18'])]),
        ]
        res = collapse(structure)
        expected = [
            ('f1', 'w1', 'd1'), ('f1', 'w1', 'd2'), ('f1', 'w1', 'd3'),
            ('f1', 'w2', 'd4'), ('f1', 'w2', 'd5'), ('f1', 'w2', 'd6'),
            ('f1', 'w3', 'd7'), ('f1', 'w3', 'd8'), ('f1', 'w3', 'd9'),
            ('f2', 'w4', 'd10'), ('f2', 'w4', 'd11'), ('f2', 'w4', 'd12'),
            ('f2', 'w5', 'd13'), ('f2', 'w5', 'd14'), ('f2', 'w5', 'd15'),
            ('f3', 'w6', 'd16'), ('f3', 'w6', 'd17'), ('f3', 'w6', 'd18'),
        ]
        self.assertEqual(res, expected)
class Test_distribute(unittest.TestCase):

    def test1(self):
        x = 1
        y = []
        res = distribute(x, y)
        expected = []
        self.assertEqual(expected, res)

    def test2(self):
        x = 1
        y = ['1', '2', '3']
        res = distribute(x, y)
        expected = [(1, '1'), (1, '2'), (1, '3')]
        self.assertEqual(expected, res)

    def test3(self):
        x = 1
        y = [[1, 1, 1], [2, 2], 3]
        res = distribute(x, y)
        expected = [[(1, 1), (1, 1), (1, 1)], [(1, 2), (1, 2)], (1, 3)]
        self.assertEqual(expected, res)

    def test4(self):
        x = 1
        y = (2, 3)
        res = distribute(x, y)
        expected = (1, 2, 3)
        self.assertEqual(expected, res)

    def test5(self):
        x = 1
        y = 2
        res = distribute(x, y)
        expected = (1, 2)
        self.assertEqual(expected, res)

if __name__ == '__main__':
    unittest.main()
