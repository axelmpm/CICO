import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')

from src.utils import collapse
from parser_utils import split_data_by, index_to_identifier, strip_newlines_at_end, factor_out_file_name
from parser_atomics import FIELD_PARSERS, parse_day_name, parse_day_weight, parse_week_num
from parser_constants import WEEK_SYMBOL, DIVIDER, INTERLINE_SEPARATOR

def parse_reg(raw_reg):
    return [(field_identifier, field_parser(raw_reg)) for field_identifier, field_parser in FIELD_PARSERS]

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
