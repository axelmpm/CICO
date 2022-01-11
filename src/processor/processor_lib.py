import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

import pandas as pd

from processor_utils import round_weight
from processor_constants import FILE, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, FIELD_KEY, FIELD_VALUE
from processor_constants import READABLE_COLUMNS, ORDERED_NO_FIELDS_COLUMNS
from src.parser.parser_fields import AGGREGABLE_FIELDS, FOOD_NAME, set_correct_field_types

def set_correct_types(data):
    data[FILE] = data[FILE].astype('string')
    data[WEEK] = data[WEEK].astype('Int32')
    data[DAY_NAME] = data[DAY_NAME].astype('string')
    data[WEIGHT] = data[WEIGHT].astype('Float32').apply(round_weight)
    data[MEAL_NUM] = data[MEAL_NUM].astype('Int32')
    return data

def into_data(regs):
    return set_correct_types(pd.DataFrame(regs, columns=[FILE, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, FIELD_KEY, FIELD_VALUE]))

def select_columns(data, columns):
    return data[[c for c in columns if c in data.columns]]

def into_readable(data):
    data = data.pivot_table(values=FIELD_VALUE, index=ORDERED_NO_FIELDS_COLUMNS, columns=FIELD_KEY, aggfunc='first', dropna=False)
    data = data.reset_index()
    data = set_correct_field_types(data)
    return select_columns(data, READABLE_COLUMNS)

def grouped_by_day(readable):
    return readable.groupby(ORDERED_NO_FIELDS_COLUMNS)[AGGREGABLE_FIELDS]

def read_data_from(dir):
    return set_correct_types(pd.read_csv(dir, index_col=0))

def into_tuples(data):
    return list(data.itertuples(index=False, name=None))

def reset_indices(data):
    return data.reset_index(drop=True)

def sort_data_by(field, data, reset_data_indices=False):  # TODO if sorted dont sort
    data = data.sort_values(field)
    return reset_indices(data) if reset_data_indices else data

def processed_regs_from(data):
    pass  # TODO

def merge(datasets):
    pass  # TODO

def process_and_store(data, path):
    data.to_csv(path)
    pass  # TODO

def get_all_food_names(data):
    return set(data[FOOD_NAME])
