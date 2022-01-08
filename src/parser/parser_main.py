import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

from re import search, sub

from src.utils import collapse
from parser_utils import split_data_by, index_to_identifier, strip_newlines_at_end, factor_out_file_name, base_atomic_parsing
from parser_food import parse_reg
from parser_constants import WEEK_SYMBOL, DIVIDER, INTERLINE_SEPARATOR, DAYS_NAMES, WEIGHT_KEYWORD, INTEGER_PATTERN, FLOAT_PATTERN

def parse_week_num(raw_week_num):
    def checker(raw_day_name):
        return bool(search(f'^ *{WEEK_SYMBOL} *[0-9]+ *: *$', raw_week_num))

    def parser(matched, raw_day_name):
        return int(sub('[^0-9]', '', raw_week_num))

    error_message = 'week format invalid'
    return base_atomic_parsing(raw_week_num, checker, parser, error_message)

def parse_day_name(raw_day_name):

    def checker(raw_day_name):
        matched = [day_name for day_name in DAYS_NAMES if day_name in raw_day_name]
        return matched

    def parser(matched, raw_day_name):
        return matched[0]

    error_message = 'day name format invalid'
    return base_atomic_parsing(raw_day_name, checker, parser, error_message)

def parse_day_weight(raw_day_weight):

    def checker(raw_day_weight):
        pattern1 = f'^ *{INTEGER_PATTERN} *(kg)? *$'
        pattern2 = f'^ *{FLOAT_PATTERN} *(kg)? *$'
        pattern3 = f'^ *{WEIGHT_KEYWORD} *:? *{INTEGER_PATTERN} *(kg)? *$'
        pattern4 = f'^ *{WEIGHT_KEYWORD} *:? *{FLOAT_PATTERN} *(kg)? *$'
        patterns = [pattern1, pattern2, pattern3, pattern4]
        return any([bool(search(pattern, raw_day_weight)) for pattern in patterns])

    def parser(matched, raw_day_weight):
        return float(sub('[^0-9\\.]', '', raw_day_weight))

    error_message = 'day weight format invalid'
    return base_atomic_parsing(raw_day_weight, checker, parser, error_message)

def parse_meal(id, raw_meal):
    return id, [parse_reg(raw_reg) for raw_reg in raw_meal]

def parse_day(raw_day):  # TODO que parse_day no se entere de la implementacion interna de la funcion que provee su input (la data esta nesteada en listas)
    content = split_data_by(INTERLINE_SEPARATOR, raw_day, inclusive=False, exact_match=True)

    if len(content) == 0 or len(content[0]) == 0:
        raise SyntaxError(f'day doesnt have day name: {raw_day}')
    else:
        try:
            day_name = parse_day_name(content[0][0])
        except SyntaxError:
            day_name = None

    if len(content) > 1 and len(content[1]) > 0:
        day_weight = parse_day_weight(content[1][0])

    return day_name, day_weight, [parse_meal(index_to_identifier(i), raw_meal) for i, raw_meal in enumerate(content[2:])]

def parse_week(raw_week):  # TODO que parse_week no se entere de la implementacion interna de la funcion que provee su input (la data esta nesteada en listas)
    content = strip_newlines_at_end(split_data_by(DIVIDER, raw_week, inclusive=False, exact_match=False))

    if len(content) != 8 or len(content[0]) == 0:
        raise SyntaxError(f'week doesnt have seven days or is lacking week number: {raw_week}')

    return parse_week_num(content[0][0]), [parse_day(raw_day) for raw_day in content[1:]]

def parse_file(raw_file):
    file_name, raw_file_content = raw_file
    return file_name, [parse_week(raw_week) for raw_week in split_data_by(WEEK_SYMBOL, raw_file_content, inclusive=True, exact_match=False) if len(raw_week) > 0]

def parse_files(files):
    return [(parse_file(raw_file)) for raw_file in files]

def parse(file_reg):
    return collapse(parse_files(factor_out_file_name(file_reg)))
