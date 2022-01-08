import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import unittest

from src.parser.parser_utils import strip_newlines_at_end, split_data_by
from src.reader.reader import read
from src.parser.parser_main import parse_week_num, parse_files, parse_day_weight, parse_day_name
from src.parser.parser_atomics import parse_food_cals, parse_food_amount, parse_food_carbs, parse_food_fat, parse_food_protein
from src.parser.parser_atomics import parse_food_name, parse_food_grams
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

    def test9(self):
        input = 'Seana 1:'
        with self.assertRaises(SyntaxError):
            parse_week_num(input)

    def test10(self):
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
        res = split_data_by(symbol, regs, True, False)
        expected = [regs[0: 3], regs[3: 5], regs[5: 6], regs[6: 8], regs[8:]]
        self.assertEqual(res, expected)

    def test2(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol___', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, True, False)
        expected = [regs[: 2], regs[2: 4], regs[4: 5], regs[5:]]
        self.assertEqual(res, expected)

    def test3(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol', 'x', 'symbol', 'symbol___', 'x', 'symbol']
        res = split_data_by(symbol, regs, True, True)
        expected = [regs[0: 3], regs[3: 5], regs[5: 8], regs[8:]]
        self.assertEqual(res, expected)

    def test4(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol', 'symbol___', 'x']
        res = split_data_by(symbol, regs, True, True)
        expected = [regs[: 2], regs[2: 4], regs[4:]]
        self.assertEqual(res, expected)

    def test5(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol___', 'x', 'symbol___', 'symbol', 'x', 'symbol']
        res = split_data_by(symbol, regs, False, False)
        expected = [regs[1: 3], regs[4: 5], regs[7:8]]
        self.assertEqual(res, expected)

    def test6(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, False, False)
        expected = [regs[: 2], regs[3: 4], regs[6:]]
        self.assertEqual(res, expected)

    def test7(self):
        symbol = 'symbol'
        regs = ['symbol', 'x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x', 'symbol']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs[1: 3], regs[4: 6], regs[7: 8]]
        self.assertEqual(res, expected)

    def test8(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs[0: 2], regs[3: 5], regs[6:]]
        self.assertEqual(res, expected)
class Test_parse_day_weight(unittest.TestCase):

    def test1(self):
        input = 'PESO: 60.2\n'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test2(self):
        input = 'PESO: 60.0'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'PESO 60.2'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test4(self):
        input = 'PESO 60.0'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test5(self):
        input = '  PESO   60.2  '
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test6(self):
        input = '  PESO   60.0  '
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test7(self):
        input = '     60.2  '
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test8(self):
        input = '     60.0  \n'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test9(self):
        input = '60.2  '
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test10(self):
        input = '60.0  '
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test11(self):
        input = '60.2'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test12(self):
        input = '60.0'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test13(self):
        input = '60'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test14(self):
        input = 'PESO60'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test15(self):
        input = 'PESO 60'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test16(self):
        input = 'PESO: 60'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test17(self):
        input = 'PESO:60'
        res = parse_day_weight(input)
        expected = 60.0
        self.assertEqual(res, expected)

    def test18(self):
        input = 'randomword 60.0'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test19(self):
        input = 'PESO randomword 60.0'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test20(self):
        input = 'randomword'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test21(self):
        input = 'PESO'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test22(self):
        input = 'randomword 60.0'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test23(self):
        input = 'PESO 60.0 60.2'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test24(self):
        input = 'PESO: 60.2kg\n'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test25(self):
        input = 'PESO: 60.2kg  \n'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test26(self):
        input = 'PESO: 60.2 kg  \n'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)

    def test27(self):
        input = '60.2 kg  \n'
        res = parse_day_weight(input)
        expected = 60.2
        self.assertEqual(res, expected)
class Test_parse_day_name(unittest.TestCase):

    def test1(self):
        input = 'Lunes:\n'
        res = parse_day_name(input)
        expected = 'Lunes'
        self.assertEqual(res, expected)

    def test2(self):
        input = 'Martes:\n'
        res = parse_day_name(input)
        expected = 'Martes'
        self.assertEqual(res, expected)

    def test3(self):
        input = 'Miercoles:\n'
        res = parse_day_name(input)
        expected = 'Miercoles'
        self.assertEqual(res, expected)

    def test4(self):
        input = 'Miércoles:\n'
        res = parse_day_name(input)
        expected = 'Miércoles'
        self.assertEqual(res, expected)

    def test5(self):
        input = 'Jueves:\n'
        res = parse_day_name(input)
        expected = 'Jueves'
        self.assertEqual(res, expected)

    def test6(self):
        input = 'Viernes:\n'
        res = parse_day_name(input)
        expected = 'Viernes'
        self.assertEqual(res, expected)

    def test7(self):
        input = 'Sabado:\n'
        res = parse_day_name(input)
        expected = 'Sabado'
        self.assertEqual(res, expected)

    def test8(self):
        input = 'Sábado:\n'
        res = parse_day_name(input)
        expected = 'Sábado'
        self.assertEqual(res, expected)

    def test9(self):
        input = 'Domingo:\n'
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test10(self):
        input = 'Domingo:  \n'
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test11(self):
        input = '  Domingo:  \n'
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test12(self):
        input = '  Domingo  :  \n'
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test13(self):
        input = '  Domingo    \n'
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test14(self):
        input = '  Domingo    '
        res = parse_day_name(input)
        expected = 'Domingo'
        self.assertEqual(res, expected)

    def test15(self):
        input = 'omingo'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test16(self):
        input = 'Domingo Domingo'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)

    def test17(self):
        input = 'DominDomingogo'
        with self.assertRaises(SyntaxError):
            parse_day_weight(input)
class Test_parse_food_protein(unittest.TestCase):

    def test1(self):
        input = 'pechuga herv    235g        393     C   67.9p'
        res = parse_food_protein(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = 'pechuga herv 235g 393 C 67p\n'
        res = parse_food_protein(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    235g        393     C  '
        res = parse_food_protein(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = 'pechuga herv    235g        393     C   67.9p\n'
        res = parse_food_protein(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = 'pechuga herv    235g        393     C   67p\n'
        res = parse_food_protein(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = 'pechuga herv    235g        393     C \n'
        res = parse_food_protein(input)
        expected = None
        self.assertEqual(res, expected)

    def test7(self):
        input = '67.9p'
        res = parse_food_protein(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test8(self):
        input = '67p'
        res = parse_food_protein(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test9(self):
        input = ''
        res = parse_food_protein(input)
        expected = None
        self.assertEqual(res, expected)

    def test10(self):
        input = '67p  '
        res = parse_food_protein(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test11(self):
        input = '67 p  '
        res = parse_food_protein(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test12(self):
        input = '67 cp  '
        res = parse_food_protein(input)
        expected = None
        self.assertEqual(res, expected)

    def test13(self):
        input = '-67p  '
        res = parse_food_protein(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test14(self):
        input = '-67.3p  '
        res = parse_food_protein(input)
        expected = -67.3
        self.assertEqual(res, expected)

class Test_parse_food_fat(unittest.TestCase):

    def test1(self):
        input = 'pechuga herv    235g        393     C   67.9f'
        res = parse_food_fat(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = 'pechuga herv 235g 393 C 67f\n'
        res = parse_food_fat(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    235g        393     C  '
        res = parse_food_fat(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = 'pechuga herv    235g        393     C   67.9f\n'
        res = parse_food_fat(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = 'pechuga herv    235g        393     C   67f\n'
        res = parse_food_fat(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = 'pechuga herv    235g        393     C \n'
        res = parse_food_fat(input)
        expected = None
        self.assertEqual(res, expected)

    def test7(self):
        input = '67.9f'
        res = parse_food_fat(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test8(self):
        input = '67f'
        res = parse_food_fat(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test9(self):
        input = ''
        res = parse_food_fat(input)
        expected = None
        self.assertEqual(res, expected)

    def test10(self):
        input = '67f  '
        res = parse_food_fat(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test11(self):
        input = '67 f  '
        res = parse_food_fat(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test12(self):
        input = '67 cf  '
        res = parse_food_fat(input)
        expected = None
        self.assertEqual(res, expected)

    def test13(self):
        input = '-67f  '
        res = parse_food_fat(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test14(self):
        input = '-67.3f  '
        res = parse_food_fat(input)
        expected = -67.3
        self.assertEqual(res, expected)

class Test_parse_food_carbs(unittest.TestCase):

    def test1(self):
        input = 'pechuga herv    235g        393     C   67.9c'
        res = parse_food_carbs(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = 'pechuga herv 235g 393 C 67c\n'
        res = parse_food_carbs(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    235g        393     C  '
        res = parse_food_carbs(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = 'pechuga herv    235g        393     C   67.9c\n'
        res = parse_food_carbs(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = 'pechuga herv    235g        393     C   67c\n'
        res = parse_food_carbs(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = 'pechuga herv    235g        393     C \n'
        res = parse_food_carbs(input)
        expected = None
        self.assertEqual(res, expected)

    def test7(self):
        input = '67.9c'
        res = parse_food_carbs(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test8(self):
        input = '67c'
        res = parse_food_carbs(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test9(self):
        input = ''
        res = parse_food_carbs(input)
        expected = None
        self.assertEqual(res, expected)

    def test10(self):
        input = '67c  '
        res = parse_food_carbs(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test11(self):
        input = '67 c  '
        res = parse_food_carbs(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test12(self):
        input = '67 cd  '
        res = parse_food_carbs(input)
        expected = None
        self.assertEqual(res, expected)

    def test13(self):
        input = '-67c  '
        res = parse_food_carbs(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test14(self):
        input = '-67.3c  '
        res = parse_food_carbs(input)
        expected = -67.3
        self.assertEqual(res, expected)

class Test_parse_food_grams(unittest.TestCase):

    def test1(self):
        input = 'pechuga herv    67.9g        393     C   100c'
        res = parse_food_grams(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = 'pechuga herv 67g 393 C 100c\n'
        res = parse_food_grams(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    235        393     C  '
        res = parse_food_grams(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = 'pechuga herv    67.9g        393     C   100c\n'
        res = parse_food_grams(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = 'pechuga herv    67g        393     C   100c\n'
        res = parse_food_grams(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = 'pechuga herv    235        393     C \n'
        res = parse_food_grams(input)
        expected = None
        self.assertEqual(res, expected)

    def test7(self):
        input = '67.9g'
        res = parse_food_grams(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test8(self):
        input = '67g'
        res = parse_food_grams(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test9(self):
        input = ''
        res = parse_food_grams(input)
        expected = None
        self.assertEqual(res, expected)

    def test10(self):
        input = '67g  '
        res = parse_food_grams(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test11(self):
        input = '67 g  '
        res = parse_food_grams(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test12(self):
        input = '67 cg  '
        res = parse_food_grams(input)
        expected = None
        self.assertEqual(res, expected)

    def test13(self):
        input = '-67g  '
        res = parse_food_grams(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test14(self):
        input = '-67.3g  '
        res = parse_food_grams(input)
        expected = -67.3
        self.assertEqual(res, expected)

class Test_parse_food_cals(unittest.TestCase):

    def test1(self):
        input = 'pechuga herv    100g        67.9     C   100c'
        res = parse_food_cals(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = 'pechuga herv 100g 67 C 100c\n'
        res = parse_food_cals(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    C  '
        res = parse_food_cals(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = 'pechuga herv    100g        67.9     C   100c\n'
        res = parse_food_cals(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = 'pechuga herv    100g        67     C   100c\n'
        res = parse_food_cals(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = '67 pechuga herv    100g    100       C   100c\n'
        res = parse_food_cals(input)
        expected = 100
        self.assertEqual(res, expected)

    def test7(self):
        input = 'pechuga herv       C \n'
        res = parse_food_cals(input)
        expected = None
        self.assertEqual(res, expected)

    def test8(self):
        input = 'pechuga herv    100g        -67     C   100c\n'
        res = parse_food_cals(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test9(self):
        input = 'pechuga herv    100g        -67.9     C   100c\n'
        res = parse_food_cals(input)
        expected = -67.9
        self.assertEqual(res, expected)

class Test_parse_food_amount(unittest.TestCase):

    def test1(self):
        input = '67.9 pechuga herv    100g      200       C   100c'
        res = parse_food_amount(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test2(self):
        input = '67 pechuga herv 100g 200 C 100c\n'
        res = parse_food_amount(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test3(self):
        input = 'pechuga herv    C  '
        res = parse_food_amount(input)
        expected = None
        self.assertEqual(res, expected)

    def test4(self):
        input = '67.9 pechuga herv    100g        200    C   100c\n'
        res = parse_food_amount(input)
        expected = 67.9
        self.assertEqual(res, expected)

    def test5(self):
        input = '67 pechuga herv    100g        200     C   100c\n'
        res = parse_food_amount(input)
        expected = 67.0
        self.assertEqual(res, expected)

    def test6(self):
        input = 'pechuga herv       C \n'
        res = parse_food_amount(input)
        expected = None
        self.assertEqual(res, expected)

    def test7(self):
        input = '-67 pechuga herv    100g             C   100c\n'
        res = parse_food_amount(input)
        expected = -67.0
        self.assertEqual(res, expected)

    def test8(self):
        input = '-67.9 pechuga herv    100g             C   100c\n'
        res = parse_food_amount(input)
        expected = -67.9
        self.assertEqual(res, expected)

class Test_parse_food_name(unittest.TestCase):

    def test1(self):
        input = '67.9 pechuga herv    100g      200       C   100c'
        res = parse_food_name(input)
        expected = 'pechuga herv'
        self.assertEqual(res, expected)

    def test2(self):
        input = '67.9 pechuga    100g      200       C   100c'
        res = parse_food_name(input)
        expected = 'pechuga'
        self.assertEqual(res, expected)

    def test3(self):
        input = '67.9 pechuga herv hoy   100g      200       C   100c'
        res = parse_food_name(input)
        expected = 'pechuga herv hoy'
        self.assertEqual(res, expected)

    def test4(self):
        input = '67.9   100g      200       C   100c'
        res = parse_food_name(input)
        expected = None
        self.assertEqual(res, expected)
class Test_parse_files(unittest.TestCase):

    def test1(self):
        file_reg = read(TEST_DATA_DIR_LARGE)
        # res = parse_files(factor_out_file_name(file_reg))
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
