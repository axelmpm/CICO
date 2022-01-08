import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')

from src.reader.reader import file_from, regs_from
from src.utils import get_indexes_of, split_into_classes

def base_atomic_parsing(raw, checker, parser, error_message, raises=True):
    if match := checker(raw):
        return parser(match)
    else:
        raise SyntaxError(f'{error_message}: {raw}') if raises else None

def float_parser(match):
    return float(match)

def int_parser(match):
    return int(match)

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

def factor_out_file_name(file_reg):
    return [(file_name, regs_from(file_reg_class)) for file_name, file_reg_class in split_into_classes(file_reg, file_from).items()]
