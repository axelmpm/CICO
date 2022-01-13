import pandas as pd
from json import load, dump

from processor_constants import NULL
from processor_utils import round_weight
from src.database.fields_constants import CARBS, FAT, FILE, PROTEIN, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, AMOUNT, FOOD_NAME, GRAMS, REG, CALS
from src.parser.parser_main import PARSER_COLUMNS_ORDER
from src.reader.reader import open_and_process_file

def set_correct_regs_db_types(data):
    data[FILE] = data[FILE].astype('string')
    data[REG] = data[REG].astype('string')
    data[WEEK] = data[WEEK].astype('Int32')
    data[DAY_NAME] = data[DAY_NAME].astype('string')
    data[WEIGHT] = data[WEIGHT].astype('Float32').apply(round_weight)
    data[MEAL_NUM] = data[MEAL_NUM].astype('Int32')
    data[FOOD_NAME] = data[FOOD_NAME].astype('string')
    data[AMOUNT] = data[AMOUNT].astype('Float32')
    data[GRAMS] = data[GRAMS].astype('Float32')
    return data

def set_correct_foods_db_types(data):
    data[FOOD_NAME] = data[FOOD_NAME].astype('string')
    data[AMOUNT] = data[AMOUNT].astype('Float32')
    data[CALS] = data[CALS].astype('Float32')
    data[PROTEIN] = data[PROTEIN].astype('Float32')
    data[CARBS] = data[CARBS].astype('Float32')
    data[FAT] = data[FAT].astype('Float32')
    return data

def into_data(regs):
    return set_correct_regs_db_types(pd.DataFrame(regs, columns=PARSER_COLUMNS_ORDER))

def select_columns(data, columns):
    return data[[c for c in columns if c in data.columns]]

def read_regs_db_from(path):
    return set_correct_regs_db_types(pd.read_csv(path, index_col=0))

def food_json_db_into_data(db):
    return pd.DataFrame(db).reset_index().rename(columns={'index': FOOD_NAME})

def read_foods_db_from(path):
    return set_correct_foods_db_types(pd.read_csv(path, index_col=0))

def reset_indices(data):
    return data.reset_index(drop=True)

def sort_data_by(field, data, reset_data_indices=False):  # TODO if sorted dont sort
    data = data.sort_values(field)
    return reset_indices(data) if reset_data_indices else data

def read_from_json(json_data, type_corrector):
    return type_corrector(pd.read_json(json_data, orient='split'))

def get_all_food_names(data):
    return set(data[FOOD_NAME])

def wrap_null_values(data):
    return data.fillna(NULL)

def data_into_json(data):
    return data.to_json(orient='split')

def data_into_records(data):
    return data.to_dict('records')

def processed_regs_from(data):
    pass  # TODO

def merge(datasets):
    pass  # TODO
