from src.utils import collapse
from parser_utils import split_data_by, index_to_identifier, strip_newlines_at_end, factor_out_file_name
from parser_atomics import parse_day_name, parse_day_weight, parse_week_num
from parser_constants import WEEK_SYMBOL, DIVIDER, INTERLINE_SEPARATOR
from parser_fields import FIELD_PARSERS
from src.database.fields_constants import FILE, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, AMOUNT, FOOD_NAME, GRAMS, REG

def parse_reg(raw_reg):
    return tuple(field_parser(raw_reg) for field_parser in FIELD_PARSERS)

def parse_meal(id, raw_meal):
    return id, [parse_reg(raw_reg) for raw_reg in raw_meal]

def parse_day(raw_day):
    content = split_data_by(INTERLINE_SEPARATOR, raw_day, include_symbol=False, exact_match=True)

    if len(content) == 0 or len(content[0]) == 0:
        raise SyntaxError(f'day doesnt have day name: {raw_day}')
    else:
        day_name = parse_day_name(content[0][0])

    day_weight = None
    if len(content) > 1 and len(content[1]) > 0:
        day_weight = parse_day_weight(content[1][0])

    start_of_meals_idx = 2 if day_weight else 1

    return day_name, day_weight, [parse_meal(index_to_identifier(i), raw_meal) for i, raw_meal in enumerate(content[start_of_meals_idx:])]

def parse_week(raw_week):
    content = strip_newlines_at_end(split_data_by(DIVIDER, raw_week, include_symbol=False, exact_match=False))

    if len(content) != 8 or len(content[0]) == 0:
        raise SyntaxError(f'week doesnt have seven days or is lacking week number: {raw_week}')

    return parse_week_num(content[0][0]), [parse_day(raw_day) for raw_day in content[1:]]

def parse_file(raw_file):
    file_name, raw_file_content = raw_file
    raw_file_content = split_data_by(WEEK_SYMBOL, raw_file_content,
                                     include_symbol=True, exact_match=False, include_first=False)
    return file_name, [parse_week(raw_week) for raw_week in raw_file_content if len(raw_week) > 0]

def parse_files(files):
    return [(parse_file(raw_file)) for raw_file in files]

def parse(file_reg):  # TODO firts component in return must be list of syntax errored
    return None, collapse(parse_files(factor_out_file_name(file_reg)))

PARSER_COLUMNS_ORDER = [FILE, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, AMOUNT, FOOD_NAME, GRAMS, REG]
