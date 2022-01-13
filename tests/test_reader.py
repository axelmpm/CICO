import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\pipeline')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\processor')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\database')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

import unittest

from src.reader.reader import read, new_regs_exist_at, regs_from, listFilesIn, directorie_of, compose_file_path, is_txt, is_cico_file
from src.paths import TEST_DATA_DIR, TEST_DATA_DIR_MEDIUM, TEST_DATA_DIR_LARGE

class Test_read(unittest.TestCase):

    def test1(self):
        file_reg = read(TEST_DATA_DIR_MEDIUM)
        self.assertIsNotNone(file_reg)
        self.assertEqual(len(file_reg), 73)

class Test_listFilesIn(unittest.TestCase):

    def test1(self):
        res = listFilesIn(TEST_DATA_DIR)
        expected = 2
        self.assertEqual(expected, len(res))
"""
class Test_new_regs_exist_at(unittest.TestCase):

    def test1(self):
        old_regs = regs_from(read(SMALL_DATA_FILES_1))
        res = new_regs_exist_at(SMALL_DATA_FILES_2, old_regs)
        expected = listFilesIn(SMALL_DATA_FILES_2)
        self.assertEqual(expected, res)

    def test2(self):
        old_regs = []
        res = new_regs_exist_at(SMALL_DATA_FILES_2, old_regs)
        expected = listFilesIn(SMALL_DATA_FILES_2)
        self.assertEqual(expected, res)

    def test3(self):
        old_regs = regs_from(read(SMALL_DATA_FILES_1))
        res = new_regs_exist_at(SMALL_DATA_FILES_1, old_regs)
        expected = []
        self.assertEqual(expected, res)
"""
class Test_directorie_of(unittest.TestCase):

    def test1(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO.txt")
        res = directorie_of(input)
        expected = TEST_DATA_DIR_LARGE
        self.assertEqual(expected, res)

    def test2(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO.txt")
        res = directorie_of(input)
        expected = TEST_DATA_DIR_LARGE
        self.assertEqual(expected, res)

class Test_is_txt(unittest.TestCase):

    def test1(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO.txt")
        res = is_txt(input)
        self.assertTrue(res)

    def test2(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICOtxt")
        res = is_txt(input)
        self.assertFalse(res)

    def test3(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO")
        res = is_txt(input)
        self.assertFalse(res)

    def test4(self):
        input = TEST_DATA_DIR_LARGE
        res = is_txt(input)
        self.assertFalse(res)
class Test_is_cico_file(unittest.TestCase):

    def test1(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO.txt")
        res = is_cico_file(input)
        self.assertTrue(res)

    def test2(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICOtxt")
        res = is_cico_file(input)
        self.assertFalse(res)

    def test3(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "historic_CICO")
        res = is_cico_file(input)
        self.assertFalse(res)

    def test4(self):
        input = TEST_DATA_DIR_LARGE
        res = is_cico_file(input)
        self.assertFalse(res)

    def test5(self):
        input = compose_file_path(TEST_DATA_DIR_LARGE, "randomfilename.txt")
        res = is_cico_file(input)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
