import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import unittest

from src.reader.reader import read
from src.parser.parser import parse_week_num, strip_newlines_at_end, split_data_by, parse
from src.paths import TEST_DATA_DIR_LARGE

class Test_parse_week_num(unittest.TestCase):

    def test1(self):
        input = 'Semana1:'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test2(self):
        input = 'Semana 1:'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test3(self):
        input = 'Semana 1:        '
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test4(self):
        input = 'Semana 1   :'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test5(self):
        input = 'Semana       1       :'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test6(self):
        input = '         Semana       1       :'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test7(self):
        input = '         Semana       1       : \n'
        res = parse_week_num(input)
        expected = 1
        self.assertEqual(res, expected)

    def test8(self):
        input = '         Semana test       1       : \n'
        with self.assertRaises(SyntaxError):
            parse_week_num(input)

    def test10(self):
        input = 'Semana 1\n\n\n'
        with self.assertRaises(SyntaxError):
            parse_week_num(input)

    def test11(self):
        input = 'Seana 1:'
        with self.assertRaises(SyntaxError):
            parse_week_num(input)

    def test12(self):
        input = 'Semana a:'
        with self.assertRaises(SyntaxError):
            parse_week_num(input)
class Test_strip_newlines_at_end(unittest.TestCase):

    def test1(self):
        input = [['t1', 't2', '\n'], ['\n'], ['t3\n'], ['\n'], ['\n']]
        res = strip_newlines_at_end(input)
        expected = [['t1', 't2', '\n'], ['\n'], ['t3\n']]
        self.assertEqual(res, expected)

    def test2(self):
        input = [['t1', 't2', '\n'], ['\n'], ['t3\n'], ['\n', '\n']]
        res = strip_newlines_at_end(input)
        expected = [['t1', 't2', '\n'], ['\n'], ['t3\n']]
        self.assertEqual(res, expected)

    def test3(self):
        input = [['t1', 't2', '\n'], ['\n'], ['t3\n']]
        res = strip_newlines_at_end(input)
        expected = [['t1', 't2', '\n'], ['\n'], ['t3\n']]
        self.assertEqual(res, expected)
class Test_split_data_by(unittest.TestCase):

    def test1(self):
        symbol = 'symbol'
        regs = ['symbol___', 'x', 'x', 'symbol___', 'x', 'symbol___', 'symbol___', 'x', 'symbol']
        res = split_data_by(symbol, regs, True, True)
        expected = [regs[0: 3], regs[3: 5], regs[5: 6], regs[6: 8], regs[8:]]
        self.assertEqual(res, expected)

    def test2(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol___', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, True, True)
        expected = [regs[: 2], regs[2: 4], regs[4: 5], regs[5:]]
        self.assertEqual(res, expected)

    def test3(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol', 'x', 'symbol', 'symbol___', 'x', 'symbol']
        res = split_data_by(symbol, regs, True, False)
        expected = [regs[0: 3], regs[3: 5], regs[5: 8], regs[8:]]
        self.assertEqual(res, expected)

    def test4(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol', 'symbol___', 'x']
        res = split_data_by(symbol, regs, True, False)
        expected = [regs[: 2], regs[2: 4], regs[4:]]
        self.assertEqual(res, expected)

    def test5(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol___', 'x', 'symbol___', 'symbol', 'x', 'symbol']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs[1: 3], regs[4: 5], regs[7:8]]
        self.assertEqual(res, expected)

    def test6(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs[: 2], regs[3: 4], regs[6:]]
        self.assertEqual(res, expected)

    def test7(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x', 'symbol']
        res = split_data_by(symbol, regs, False, False)
        expected = [regs[1: 3], regs[4: 6], regs[7: 8]]
        self.assertEqual(res, expected)

    def test8(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, False, False)
        expected = [regs[0: 2], regs[3: 5], regs[6:]]
        self.assertEqual(res, expected)
class Test_parse(unittest.TestCase):

    def test1(self):
        file_reg = read(TEST_DATA_DIR_LARGE)
        res = parse(file_reg)
        self.assertEqual(res)

if __name__ == '__main__':
    unittest.main()
