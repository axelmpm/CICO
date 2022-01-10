import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import unittest

from src.parser.parser_utils import strip_newlines_at_end, split_data_by
from src.reader.reader import read
from src.parser.parser_main import parse_reg, parse_meal, parse_day, parse_week, parse_file, parse
from src.parser.parser_fields import parse_food_cals, parse_food_amount, parse_food_carbs, parse_food_fat, parse_food_protein, parse_food_grams, parse_food_name
from src.parser.parser_atomics import parse_week_num, parse_day_weight, parse_day_name
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

    def test9(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'x']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs]
        self.assertEqual(res, expected)

    def test10(self):
        symbol = 'symbol'
        regs = ['x']
        res = split_data_by(symbol, regs, False, True)
        expected = [regs]
        self.assertEqual(res, expected)

    def test11(self):
        symbol = 'symbol'
        regs = ['x', 'x', 'symbol', 'x', 'symbol___', 'symbol', 'x']
        res = split_data_by(symbol, regs, False, True, False)
        expected = [regs[3: 5], regs[6:]]
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
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test19(self):
        input = 'PESO randomword 60.0'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test20(self):
        input = 'randomword'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test21(self):
        input = 'PESO'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test22(self):
        input = 'randomword 60.0'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test23(self):
        input = 'PESO 60.0 60.2'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

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
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test16(self):
        input = 'Domingo Domingo'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)

    def test17(self):
        input = 'DominDomingogo'
        res = parse_day_weight(input)
        expected = None
        self.assertEqual(res, expected)
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

class Test_parse_reg(unittest.TestCase):

    def test1(self):
        input = '2 long name food 100 200g 10p 5c 3f\n'
        res = [value for _, value in parse_reg(input)]
        expected = [2.0, 'long name food', 100.0, 200.0, 10.0, 5.0, 3.0]
        self.assertEqual(res, expected)

    def test2(self):
        input = 'long name food 100 200g 10p 5c 3f\n'
        res = [value for _, value in parse_reg(input)]
        expected = [None, 'long name food', 100.0, 200.0, 10.0, 5.0, 3.0]
        self.assertEqual(res, expected)

    def test3(self):
        input = 'long name food 100 200g'
        res = [value for _, value in parse_reg(input)]
        expected = [None, 'long name food', 100.0, 200.0, None, None, None]
        self.assertEqual(res, expected)

    def test4(self):
        input = 'long name food 200g'
        res = [value for _, value in parse_reg(input)]
        expected = [None, 'long name food', None, 200.0, None, None, None]
        self.assertEqual(res, expected)

    def test5(self):
        input = '2.0 long name food 200g'
        res = [value for _, value in parse_reg(input)]
        expected = [2.0, 'long name food', None, 200.0, None, None, None]
        self.assertEqual(res, expected)

    def test6(self):
        input = '2.5 200.5'
        res = [value for _, value in parse_reg(input)]
        expected = [None, None, None, None, None, None, None]
        self.assertEqual(res, expected)

    def test7(self):
        input = '200'
        res = [value for _, value in parse_reg(input)]
        expected = [None, None, None, None, None, None, None]
        self.assertEqual(res, expected)

class Test_parse_meal(unittest.TestCase):

    def test1(self):
        id = 1
        input = [
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            'long 100 200g 10p 5c 3f\n',
            'long name food 100 200g 10p 5c 3f\n']
        res = parse_meal(id, input)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], 1)
        self.assertIsInstance(res[1], list)
        self.assertEqual(len(res[1]), 4)

class Test_parse_day(unittest.TestCase):

    def test1(self):
        input = [
            'Lunes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            '\n',
            'long 100 200g 10p 5c 3f\n',
            'long name food 100 200g 10p 5c 3f\n',
            '\n']
        res = parse_day(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 'Lunes')
        self.assertEqual(res[1], 63.7)
        self.assertIsInstance(res[2], list)
        self.assertEqual(len(res[2]), 2)

    def test2(self):
        input = [
            'Lunes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            'long 100 200g 10p 5c 3f\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            '\n']
        res = parse_day(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 'Lunes')
        self.assertEqual(res[1], 63.7)
        self.assertIsInstance(res[2], list)
        self.assertEqual(len(res[2]), 2)

    def test3(self):
        input = [
            'Lunes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            'long 100 200g 10p 5c 3f\n',
            'long name food 100 200g 10p 5c 3f\n',
            '\n',
            '\n']
        res = parse_day(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 'Lunes')
        self.assertEqual(res[1], 63.7)
        self.assertIsInstance(res[2], list)
        self.assertEqual(len(res[2]), 1)

    def test4(self):
        input = [
            'Lunes:\n',
            '\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            'long 100 200g 10p 5c 3f\n',
            'long name food 100 200g 10p 5c 3f\n',
            '\n',
            '\n']
        res = parse_day(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 'Lunes')
        self.assertEqual(res[1], None)
        self.assertIsInstance(res[2], list)
        self.assertEqual(len(res[2]), 1)

    def test5(self):
        input = [
            'Lunes:\n',
            '\n',
            '\n',
            '\n']
        res = parse_day(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 'Lunes')
        self.assertEqual(res[1], None)
        self.assertIsInstance(res[2], list)
        self.assertEqual(len(res[2]), 0)

    def test6(self):
        input = [
            '\n',
            '\n',
            'long name food 100 200g 10p 5c 3f\n',
            'long name 100 200g 10p 5c 3f\n',
            'long 100 200g 10p 5c 3f\n',
            'long name food 100 200g 10p 5c 3f\n',
            '\n',
            '\n']
        with self.assertRaises(SyntaxError):
            parse_day(input)
class Test_parse_week(unittest.TestCase):

    def test1(self):
        input = [
            'Semana 18:\n',
            '\n',
            '\n',
            '#----------------------------------------------------------------------\n',
            '\n',
            '\n',
            'Lunes:\n',
            '\n',
            '\n',
            'PESO: 63.9kg\n',
            '\n',
            '\n',
            '\n',
            '1 cafe          -           0       A\n',
            '1 cafe G        -           0       A\n',
            'carne           155g        240     C\n',
            '30 papa         240g        195     V\n',
            '25 batata       250g        225     V\n',
            'carne           55g         90      C\n',
            '\n',
            'arroz           200g        220     V\n',
            'roquefort       40g         145     E\n',
            'pan             70g         175     E\n',
            '1 alfajor       50g         205     E\n',
            '1 leche         -           90      E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Martes:\n',
            '\n',
            'PESO: 64.2kg\n',
            '\n',
            'mantecol        25g         125     E\n',
            'turron arcor    25g         100     E\n',
            'carne           180g        270     C\n',
            'arroz           200g        220     V\n',
            'aceite          13g         108     O\n',
            'carne           180g        270     C\n',
            '2 vainillas     24g         89      E\n',
            'berenjena       50g         15      V\n',
            'cebolla         35g         15      V\n',
            'durazno         200g        150     E|F\n',
            'crema           100g        350     E\n',
            '5 agua          2500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 64.0kg\n',
            '\n',
            '2 huevo frito   90g         140     C\n',
            'crema           50g         175     E\n',
            'durazno         135g        101     E|F\n',
            '2.5 pan verde   63g         150     E\n',
            'manteca         15g         113     E\n',
            '6 pan           180g        450     E\n',
            '0.5 leche       -           45      E\n',
            '0.5 pionono hue 90g         155     E|C[30]|V[30]\n',
            '0.5 pionono pal 90g         137     E|C[30]|V[30]\n',
            '0.5 pionono atu 90g         147     E|C[30]|V[30]\n',
            '1 pionono hue   175g        301     E|C[30]|V[30]\n',
            'bondiola        130g        343     C\n',
            '4 agua          2000g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 64.3kg\n',
            '\n',
            '1.25 rosario    200g        485     E\n',
            '2 pionono hue   300g        516     E|C[30]|V[30]\n',
            '\n',
            'bondiola        170g        449     C\n',
            'rosario cafe    100g        300     E\n',
            '2 leche         -           180     E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            '3 pionono hue   360g        620     E|C[30]|V[30]\n',
            'bondiola        200g        528     C\n',
            '10 papa         100g        77      V\n',
            '2 pan bimbo     65g         170     E\n',
            '4 mostaza       48g         20      E\n',
            '15 bolls        20g         90      E\n',
            '1 rosario       250g        600     E\n',
            '0.5 leche       -           45      E\n',
            '4 pionono hue   400g        688     E|C[30]|V[30]\n',
            '10 papa         100g        77      V\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 64.0kg\n',
            '----------------------------------------------------------------------\n',
            '\n',
            '\n',
            '\n',
            '\n']
        res = parse_week(input)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], 18)
        self.assertIsInstance(res[1], list)
        self.assertEqual(len(res[1]), 7)

    def test2(self):
        input = [
            '#----------------------------------------------------------------------\n',
            'Lunes:\n',
            '\n',
            'PESO: 63.9kg\n',
            '\n',
            '1 cafe          -           0       A\n',
            '1 cafe G        -           0       A\n',
            'carne           155g        240     C\n',
            '30 papa         240g        195     V\n',
            '25 batata       250g        225     V\n',
            'carne           55g         90      C\n',
            '\n',
            'arroz           200g        220     V\n',
            'roquefort       40g         145     E\n',
            'pan             70g         175     E\n',
            '1 alfajor       50g         205     E\n',
            '1 leche         -           90      E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Martes:\n',
            '\n',
            'PESO: 64.2kg\n',
            '\n',
            'mantecol        25g         125     E\n',
            'turron arcor    25g         100     E\n',
            'carne           180g        270     C\n',
            'arroz           200g        220     V\n',
            'aceite          13g         108     O\n',
            'carne           180g        270     C\n',
            '2 vainillas     24g         89      E\n',
            'berenjena       50g         15      V\n',
            'cebolla         35g         15      V\n',
            'durazno         200g        150     E|F\n',
            'crema           100g        350     E\n',
            '5 agua          2500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 64.0kg\n',
            '\n',
            '2 huevo frito   90g         140     C\n',
            'crema           50g         175     E\n',
            'durazno         135g        101     E|F\n',
            '2.5 pan verde   63g         150     E\n',
            'manteca         15g         113     E\n',
            '6 pan           180g        450     E\n',
            '0.5 leche       -           45      E\n',
            '0.5 pionono hue 90g         155     E|C[30]|V[30]\n',
            '0.5 pionono pal 90g         137     E|C[30]|V[30]\n',
            '0.5 pionono atu 90g         147     E|C[30]|V[30]\n',
            '1 pionono hue   175g        301     E|C[30]|V[30]\n',
            'bondiola        130g        343     C\n',
            '4 agua          2000g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 64.3kg\n',
            '\n',
            '1.25 rosario    200g        485     E\n',
            '2 pionono hue   300g        516     E|C[30]|V[30]\n',
            '\n',
            'bondiola        170g        449     C\n',
            'rosario cafe    100g        300     E\n',
            '2 leche         -           180     E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            '3 pionono hue   360g        620     E|C[30]|V[30]\n',
            'bondiola        200g        528     C\n',
            '10 papa         100g        77      V\n',
            '2 pan bimbo     65g         170     E\n',
            '4 mostaza       48g         20      E\n',
            '15 bolls        20g         90      E\n',
            '1 rosario       250g        600     E\n',
            '0.5 leche       -           45      E\n',
            '4 pionono hue   400g        688     E|C[30]|V[30]\n',
            '10 papa         100g        77      V\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 64.0kg\n',
            '----------------------------------------------------------------------\n',
            '\n',
            '\n',
            '\n',
            '\n']
        with self.assertRaises(SyntaxError):
            parse_week(input)

    def test3(self):
        input = [
            'Semana 18:\n',
            '#----------------------------------------------------------------------\n',
            'Lunes:\n',
            '\n',
            'PESO: 63.9kg\n',
            '\n',
            '1 cafe          -           0       A\n',
            '1 cafe G        -           0       A\n',
            'carne           155g        240     C\n',
            '30 papa         240g        195     V\n',
            '25 batata       250g        225     V\n',
            'carne           55g         90      C\n',
            '\n',
            'arroz           200g        220     V\n',
            'roquefort       40g         145     E\n',
            'pan             70g         175     E\n',
            '1 alfajor       50g         205     E\n',
            '1 leche         -           90      E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 64.0kg\n',
            '\n',
            '2 huevo frito   90g         140     C\n',
            'crema           50g         175     E\n',
            'durazno         135g        101     E|F\n',
            '2.5 pan verde   63g         150     E\n',
            'manteca         15g         113     E\n',
            '6 pan           180g        450     E\n',
            '0.5 leche       -           45      E\n',
            '0.5 pionono hue 90g         155     E|C[30]|V[30]\n',
            '0.5 pionono pal 90g         137     E|C[30]|V[30]\n',
            '0.5 pionono atu 90g         147     E|C[30]|V[30]\n',
            '1 pionono hue   175g        301     E|C[30]|V[30]\n',
            'bondiola        130g        343     C\n',
            '4 agua          2000g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 64.3kg\n',
            '\n',
            '1.25 rosario    200g        485     E\n',
            '2 pionono hue   300g        516     E|C[30]|V[30]\n',
            '\n',
            'bondiola        170g        449     C\n',
            'rosario cafe    100g        300     E\n',
            '2 leche         -           180     E\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            '3 pionono hue   360g        620     E|C[30]|V[30]\n',
            'bondiola        200g        528     C\n',
            '10 papa         100g        77      V\n',
            '2 pan bimbo     65g         170     E\n',
            '4 mostaza       48g         20      E\n',
            '15 bolls        20g         90      E\n',
            '1 rosario       250g        600     E\n',
            '0.5 leche       -           45      E\n',
            '4 pionono hue   400g        688     E|C[30]|V[30]\n',
            '10 papa         100g        77      V\n',
            '3 agua          1500g       0       A\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 64.0kg\n',
            '----------------------------------------------------------------------\n',
            '\n',
            '\n',
            '\n',
            '\n']
        with self.assertRaises(SyntaxError):
            parse_week(input)
class Test_parse_file(unittest.TestCase):

    def test1(self):
        file_name = 'file_name'
        input = [
            '\n',
            '\n',
            '\n',
            '\n',
            'Semana 4:\n',
            '#----------------------------------------------------------------------\n',
            'Lunes:\n',
            '\n',
            'PESO: 63.7kg\n',
            '\n',
            '1 salchicha     35g     80      C\n',
            '1 hamburguesa   50g     100     C\n',
            'carne           130g    200     C\n',
            '1 sardina       90g     120     P\n',
            'zapallo         190g    40      V\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Martes:\n',
            '\n',
            'PESO: 63.3kg\n',
            '\n',
            '3 salchicha     105g    240     C\n',
            '1 hamburguesa   50g     100     C\n',
            'guiso salchi    330g    330     V|C[15]\n',
            'guiso salchi    380g    380     V|C[15]\n',
            '1 tomate        180g    35      V\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 63.1kg\n',
            '\n',
            'guiso salchi    520g    520     V|C[15]\n',
            '2 manzanas      230g    115     F\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 63.3kg\n',
            '\n',
            'tarta atun      620g    620     V|P[30]|E[20]\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 63.4kg\n',
            '\n',
            'tarta atun      400g    400     V|P[30]|E[20]\n',
            'tarta atun RQ   55g     95      V|P[30]|E[40]\n',
            'chichulin       100g    85      C\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '\n',
            'PESO: 62.4kg\n',
            '\n',
            '1 huevo frito   45g     70      C\n',
            'guiso salchi    505g    505     V|C[15]\n',
            'carne           320g    460     C\n',
            'tomate          260g    55      V\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 62.6kg\n',
            '\n',
            'carne           310g    455     C\n',
            '0.5 tomate      110g    25      V\n',
            '2 huevo frito   90g     140     C\n',
            '2 pepas         30g     125     E\n',
            '0.34 leche       84g     30      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Semana 5:\n',
            '#----------------------------------------------------------------------\n',
            'Lunes:\n',
            '\n',
            'PESO: 62.0kg\n',
            '\n',
            '3 salchicha     105g    240     C\n',
            'pollo           320g    460     C\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Martes:\n',
            '\n',
            'PESO: 61.8kg\n',
            '\n',
            'arroz           215g    240     V\n',
            'aceite          20g     170     O  \n',
            '1 banana        115g    105     F\n',
            '1 leche         250g    90      E\n',
            '2 pepas         30g     125     E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 62.0kg\n',
            '\n',
            'carne           35g     60      C\n',
            '1 mandarina     100g    50      F\n',
            'arroz           280g    310     V\n',
            'aceite          27g     225     O\n',
            '1 banana        120g    105     F\n',
            '1 leche         -       90      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 61.4kg\n',
            '\n',
            'jugo naranja    465g    210     F\n',
            'pollo           170g    255     C\n',
            'tarta atun      400g    400     V|P[30]|E[20]\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 61.6kg\n',
            '\n',
            'tarta atun      500g    500     V|P[30]|E[20]\n',
            '1 mandarina     90g     45      F\n',
            '1 naranja       90g     35      F\n',
            '1 banana        110g    100     F\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '\n',
            'PESO: 61.3kg\n',
            '\n',
            'zapallo         240g    60      V\n',
            'morron          50g     20      V\n',
            'carne           410g    615     C\n',
            '4 pepas         60g     250     E\n',
            '1 leche         -       90      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 61.7kg\n',
            '\n',
            '2 naranja       385g    155     F\n',
            '1 manzana       240g    120     F\n',
            'carne           300g    450     C\n',
            'zanahoria       120g    50      V\n',
            'apio            60g     10      V\n',
            '2.5 pepas       45g     185     E\n',
            '1 leche         -       90      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            '\n',
            '\n',
            '\n',
            'Semana 6:\n',
            '#----------------------------------------------------------------------\n',
            'Lunes:\n',
            '\n',
            'PESO: 62.0kg\n',
            '\n',
            'carne           290g    435     C\n',
            '2.5 leche       -       225     E\n',
            'nesquick        22g     85      E\n',
            '2 banana        215g    115     F\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Martes:\n',
            '\n',
            'PESO: 62.1kg\n',
            '\n',
            'dulce leche     100g    320     E\n',
            'casamcrem       70g     165     E\n',
            '2 pan bimbo     65g     170     E\n',
            '1 leche         -       90      E\n',
            '3 hamburguesa   170g    340     C\n',
            '4 pan verde     100g    220     E\n',
            'cebolla         60g     25      V\n',
            'tomate          65g     15      V\n',
            'mayonesa        25g     50      E\n',
            '2 huevo frito   90g     140     C\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Miercoles:\n',
            '\n',
            'PESO: 62.0kg\n',
            '\n',
            'nachos          60g     295     E\n',
            'cheddar         110g    230     E\n',
            '3D              10g     50      E\n',
            'salmon          230g    345     P\n',
            '1 hamburguesa   55g     110     C\n',
            'mayonesa        25g     50      E\n',
            '8 chocolinas    55g     240     E\n',
            'chotorta mezcla 80g     220     E\n',
            '1 leche         -       90      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Jueves:\n',
            '\n',
            'PESO: 61.9kg\n',
            '\n',
            '3 taco morron   570g    1140    V[20]|C[23]|E\n',
            '2 taco guaca    380g    830     V[20]|C[23]|E\n',
            'nachos          60g     295     E\n',
            '50 aros ceb     315g    470     E|V        \n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Viernes:\n',
            '\n',
            'PESO: 62.0kg\n',
            '2 taco guaca    380g    830     V[20]|C[23]|E\n',
            '25 aros ceb     155g    235     E|V   \n',
            '1 leche         -       90      E\n',
            '3 dulce leche   60g     195     E\n',
            '3 vainilla      45g     165     E\n',
            'chocotorta      350g    1050    E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Sabado:\n',
            '\n',
            'PESO: 62.5kg\n',
            '\n',
            'chocotorta      300g    900     E\n',
            '1 leche         -       90      E\n',
            '4 hamburguesa   220g    440     C\n',
            '4 pan verde     100g    220     E\n',
            'tomate          30g     5       V\n',
            'cebolla         30g     15      V\n',
            'guacamole       100g    130     V\n',
            'sour cream      60g     200     E\n',
            '5 aros ceb      30g     45      E\n',
            '1 rapidita      30g     80      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            'Domingo:\n',
            '\n',
            'PESO: 62.7kg\n',
            '\n',
            '8 taco guaca    1425g   3115    V[20]|C[23]|E\n',
            '10 aros ceb     60g     90      E\n',
            '0.5 pan blanco  20g     40      E\n',
            '\n',
            '----------------------------------------------------------------------\n',
            '\n',
            '\n']
        res = parse_file((file_name, input))
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], file_name)
        self.assertIsInstance(res[1], list)
        self.assertEqual(len(res[1]), 3)

class Test_parse(unittest.TestCase):

    def test1(self):
        input = read(TEST_DATA_DIR_LARGE)
        _, res = parse(input)
        self.assertIsInstance(res, list)
        self.assertTrue(all([type(reg) == tuple and len(reg) > 5 for reg in res]))

if __name__ == '__main__':
    unittest.main()
