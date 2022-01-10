import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')

from parser_constants import NUMBER_PATTERN, FOOD_NAME_PATTERN
from parser_atomics import base_atomic_parsing, float_parser, unit_checker
from parser_utils import remove_white_spaces_at_start_and_end
from src.utils import matches_with

GRAMS = 'grams'
CALS = 'cals'
AMOUNT = 'amount'
PROTEIN = 'protein'
CARBS = 'carbs'
FAT = 'fat'
WATER = 'water',
FOOD_NAME = 'food'
SALT = 'salt'
FIBER = 'fiber',
GLYCEMIC_INDEX = 'glycemic index'
QUALITY = 'quality'
RAW_REG = 'register'

FIELDS_ORDER = [FOOD_NAME, AMOUNT, GRAMS, CALS, PROTEIN, CARBS, FAT, WATER, SALT, FIBER, GLYCEMIC_INDEX, QUALITY, RAW_REG]

def parse_food_grams(raw_reg):
    error_message = 'invalid grams format'
    return base_atomic_parsing(raw_reg, unit_checker('g'), float_parser, error_message, raises=False)

def parse_food_carbs(raw_reg):
    error_message = 'invalid carbs format'
    return base_atomic_parsing(raw_reg, unit_checker('c'), float_parser, error_message, raises=False)

def parse_food_fat(raw_reg):
    error_message = 'invalid fat format'
    return base_atomic_parsing(raw_reg, unit_checker('f'), float_parser, error_message, raises=False)

def parse_food_protein(raw_reg):
    error_message = 'invalid protein format'
    return base_atomic_parsing(raw_reg, unit_checker('p'), float_parser, error_message, raises=False)

def parse_food_cals(raw_reg):

    def checker(raw_reg):
        pattern = f'^.*({FOOD_NAME_PATTERN}).*?({NUMBER_PATTERN})(\\s.*|$)'
        patterns = [pattern]
        target = NUMBER_PATTERN
        return matches_with(patterns, target, raw_reg)

    error_message = 'invalid cals format'
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_amount(raw_reg):

    def checker(raw_reg):
        pattern = f'^\\s*?({NUMBER_PATTERN})\\s*({FOOD_NAME_PATTERN}).*$'
        patterns = [pattern]
        target = NUMBER_PATTERN
        return matches_with(patterns, target, raw_reg)

    error_message = 'invalid amount format'
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_name(raw_reg):

    def checker(raw_reg):
        pattern = f'^.*?({FOOD_NAME_PATTERN}).*$'
        patterns = [pattern]
        target = FOOD_NAME_PATTERN
        return matches_with(patterns, target, raw_reg)

    def parser(matched):
        parsed = remove_white_spaces_at_start_and_end(matched)
        return parsed if len(parsed) > 0 else None

    error_message = 'invalid name format'
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_raw_reg(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched):
        return matched

    error_message = 'INTERNAL ERROR, <RAW REG> SHOUDNT RAISE ERROR'
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

FIELD_PARSERS = [
    (AMOUNT, parse_food_amount),
    (FOOD_NAME, parse_food_name),
    (CALS, parse_food_cals),
    (GRAMS, parse_food_grams),
    (PROTEIN, parse_food_protein),
    (CARBS, parse_food_carbs),
    (FAT, parse_food_fat),
    (RAW_REG, parse_raw_reg),
]
