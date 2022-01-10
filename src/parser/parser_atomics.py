import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')

from src.utils import matches_with
from parser_constants import WEEK_SYMBOL, DAYS_NAMES, WEIGHT_PATTERN, NUMBER_PATTERN, INTEGER_PATTERN

def float_parser(match):
    return float(match)

def int_parser(match):
    return int(match)

def unit_checker(unit):
    def checker(raw_reg):
        pattern = f'^.*?({NUMBER_PATTERN})\\s*{unit}(\\s.*|)$'
        patterns = [pattern]
        target = NUMBER_PATTERN
        return matches_with(patterns, target, raw_reg)
    return checker

def base_atomic_parsing(raw, checker, parser, error_message, raises=True):
    if match := checker(raw):
        return parser(match)
    else:
        if raises:
            raise SyntaxError(f'{error_message}: {raw}')
        else:
            return None

def parse_week_num(raw_week_num):

    def checker(raw_week_num):
        pattern = f'^\\s*{WEEK_SYMBOL}\\s*({INTEGER_PATTERN})\\s*:?\\s*$'
        patterns = [pattern]
        target = INTEGER_PATTERN
        return matches_with(patterns, target, raw_week_num)

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
        pattern = f'^\\s*({WEIGHT_PATTERN})?\\s*({NUMBER_PATTERN})\\s*(kg)?\\s*$'
        patterns = [pattern]
        target = NUMBER_PATTERN
        return matches_with(patterns, target, raw_day_weight)

    error_message = 'day weight format invalid'
    return base_atomic_parsing(raw_day_weight, checker, float_parser, error_message, raises=False)
