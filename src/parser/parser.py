import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

from re import search, sub

from src.reader.reader import file_from, regs_from
from src.utils import get_indexes_of, split_into_classes, collapse
from parser_constants import WEEK_SYMBOL, DIVIDER, INTERLINE_SEPARATOR, DAYS_NAMES, WEIGHT_KEYWORD, INTEGER_PATTERN, FLOAT_PATTERN
from parser_food import parse_reg

def identifier_to_index(i):
    return i - 1

def index_to_identifier(i):
    return i + 1

def split_data_by(symbol, regs, inclusive=True, exact_match=True):
    indices = get_indexes_of(symbol, regs, exact_match=exact_match)
    if len(indices) > 0:
        first = [regs[:indices[0]]]
        if inclusive:
            last = [regs[indices[-1]:]]
            middle = [regs[current_idx: next_idx] for current_idx, next_idx in zip(indices, indices[1:])]
        else:
            last = [regs[indices[-1] + 1:]] if indices[-1] + 1 < len(regs) else []
            middle = [regs[current_idx + 1: next_idx] for current_idx, next_idx in zip(indices, indices[1:]) if current_idx + 1 < next_idx]

        slices = first + middle + last
    else:
        slices = []

    return [s for s in slices if len(s) > 0]

def strip_newlines_at_end(sequence):
    for i, e in enumerate(sequence[::-1]):
        if all(['\n' == x for x in e]):
            continue
        else:
            return sequence[:-i] if i > 0 else sequence
    return sequence

def parse_week_num(raw_week_num):
    if bool(search(f'^ *{WEEK_SYMBOL} *[0-9]+ *: *$', raw_week_num)):
        return int(sub('[^0-9]', '', raw_week_num))
    else:
        raise SyntaxError(f'week format invalid: {raw_week_num}')

def parse_day_name(raw_day_name):
    matched = [day_name for day_name in DAYS_NAMES if day_name in raw_day_name]
    if len(matched) > 1:
        raise SyntaxError(f'cant have more than one day name: {raw_day_name}')
    elif len(matched) == 1:
        return matched[0]
    else:
        raise SyntaxError(f'day name format invalid: {raw_day_name}')

def parse_day_weight(raw_day_weight):
    pattern1 = f'^ *{INTEGER_PATTERN} *(kg)? *$'
    pattern2 = f'^ *{FLOAT_PATTERN} *(kg)? *$'
    pattern3 = f'^ *{WEIGHT_KEYWORD} *:? *{INTEGER_PATTERN} *(kg)? *$'
    pattern4 = f'^ *{WEIGHT_KEYWORD} *:? *{FLOAT_PATTERN} *(kg)? *$'
    patterns = [pattern1, pattern2, pattern3, pattern4]
    if any([bool(search(pattern, raw_day_weight)) for pattern in patterns]):
        return float(sub('[^0-9\\.]', '', raw_day_weight))
    else:
        raise SyntaxError(f'day weight format invalid: {raw_day_weight}')

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

def factor_out_file_name(file_reg):
    return [(file_name, regs_from(file_reg_class)) for file_name, file_reg_class in split_into_classes(file_reg, file_from).items()]

def parse_files(files):
    return [(parse_file(raw_file)) for raw_file in files]

def parse(file_reg):
    return collapse(parse_files(factor_out_file_name(file_reg)))
