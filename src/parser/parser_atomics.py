import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')

from enum import Enum

from src.utils import matches_with, do_nothing
from parser_utils import base_atomic_parsing, float_parser, int_parser
from parser_constants import WEEK_SYMBOL, DAYS_NAMES, WEIGHT_KEYWORD, INTEGER_PATTERN, FLOAT_PATTERN

class FieldIdentifier(Enum):
    GRAMS = 1
    CALS = 2
    AMOUNT = 3
    CARBS = 4
    FAT = 5
    PROTEIN = 6
    WATER = 7
    FOOD_NAME = 8
    SALT = 9
    FIBER = 10
    GLYCEMIC_INDEX = 11
    QUALITY = 12

def parse_food_grams(raw_reg):

    def checker(raw_reg):
        pattern1 = f'^.*?({FLOAT_PATTERN}) *p *$'
        pattern2 = f'^.*?({INTEGER_PATTERN}) *p *$'
        patterns = [pattern1, pattern2]
        return matches_with(patterns, raw_reg)

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_cals(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_amount(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_carbs(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_fat(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_protein(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, float_parser, error_message, raises=False)

def parse_food_name(raw_reg):

    def checker(raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, do_nothing, error_message, raises=False)

def parse_food_quality(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched):
        return matched

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_week_num(raw_week_num):
    def checker(raw_day_name):
        patterns = [f'^ *{WEEK_SYMBOL} *([0-9]+) *: *$']
        return matches_with(patterns, raw_week_num)

    error_message = 'week format invalid'
    return base_atomic_parsing(raw_week_num, checker, int_parser, error_message)

def parse_day_name(raw_day_name):

    def checker(raw_day_name):
        matched = [day_name for day_name in DAYS_NAMES if day_name in raw_day_name]
        return matched

    def parser(matched):
        return matched[0]

    error_message = 'day name format invalid'
    return base_atomic_parsing(raw_day_name, checker, parser, error_message)

def parse_day_weight(raw_day_weight):

    def checker(raw_day_weight):
        pattern1 = f'^ *{WEIGHT_KEYWORD} *:? *({FLOAT_PATTERN}) *(kg)? *$'
        pattern2 = f'^ *({FLOAT_PATTERN}) *(kg)? *$'
        pattern3 = f'^ *({INTEGER_PATTERN}) *(kg)? *$'
        pattern4 = f'^ *{WEIGHT_KEYWORD} *:? *({INTEGER_PATTERN}) *(kg)? *$'
        patterns = [pattern1, pattern2, pattern3, pattern4]
        return matches_with(patterns, raw_day_weight)

    error_message = 'day weight format invalid'
    return base_atomic_parsing(raw_day_weight, checker, float_parser, error_message)

FIELD_PARSERS = [
    (FieldIdentifier.GRAMS, parse_food_grams),
    (FieldIdentifier.CALS, parse_food_cals),
    (FieldIdentifier.AMOUNT, parse_food_amount),
    (FieldIdentifier.CARBS, parse_food_carbs),
    (FieldIdentifier.FAT, parse_food_fat),
    (FieldIdentifier.PROTEIN, parse_food_protein),
    (FieldIdentifier.FOOD_NAME, parse_food_name),
    (FieldIdentifier.QUALITY, parse_food_quality),
]
