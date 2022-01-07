import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

from re import search, sub

from src.reader.reader import file_from
from src.utils import get_indexes_of, split_into_classes, collapse
from parser_constants import WEEK_SYMBOL, DIVIDER

def identifier_to_index(i):
    return i - 1

def index_to_identifier(i):
    return i + 1

def split_data_by(symbol, regs, inclusive=True, containing=False):
    indices = get_indexes_of(symbol, regs, containing=containing)
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
    return [e for e in sequence if '\n' not in e]

def parse_week_num(raw_week_num):
    if bool(search(f'^ *{WEEK_SYMBOL} *[0-9]+ *: *$', raw_week_num)):
        return int(sub('[^0-9]', '', raw_week_num))
    else:
        raise SyntaxError(f'week format invalid: {raw_week_num}')

def parse_day(raw_day):
    return (None, None)

def parse_week(raw_week):
    content = strip_newlines_at_end(split_data_by(DIVIDER, raw_week, inclusive=False, containing=True))

    if len(content) != 8 or len(content[0]) == 0:
        raise SyntaxError(f'week doesent have seven days or is lacking week number: {raw_week}')

    week_num, days = parse_week_num(content[0][0]), [parse_day(raw_day) for raw_day in content[1:]]
    # return distribute(week_num, days)

def parse_file(raw_file):
    return [parse_week(raw_week) for raw_week in split_data_by(WEEK_SYMBOL, raw_file, inclusive=True, containing=True) if len(raw_week) > 0]

def into_files_with_weeks(file_reg):
    return [(file_name, [reg for _, reg in regs]) for file_name, regs in split_into_classes(file_reg, file_from).items()]

def parse(file_reg):
    return collapse([(file_name, parse_file(raw_file)) for file_name, raw_file in into_files_with_weeks(file_reg)])
