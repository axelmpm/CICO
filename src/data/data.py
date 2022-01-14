import pandas as pd
from json import load

from src.paths import PROCESSED_DATA, HISTORIC_DATA, DB_DATA
from src.reader.reader import read, open_and_process_file
from src.parser.parser_main import parse, PARSER_COLUMNS_ORDER
from data_constants import CARBS, FAT, FILE, PROTEIN, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, AMOUNT, FOOD_NAME, GRAMS, REG, CALS, NULL, LEGACY_METADATA
from data_utils import round_weight

class Data:

    @classmethod
    def load(cls):
        try:
            data = cls.read()
        except FileNotFoundError:
            data = cls.build()
            cls.store(data)
        return cls(data)

    @classmethod
    def read(cls):
        return cls.initialize(pd.read_csv(cls.processed_data_path, index_col=0))

    @classmethod
    def store(cls, data):
        data.to_csv(cls.processed_data_path)

    @classmethod
    def initialize(cls, data):
        data = cls.initialize_types(data)
        data = cls.post_process(data)
        data = cls.wrap_null_values(data)
        data = cls.order_columns(data)
        return data

    @classmethod
    def from_cacheable_to_data(cls, cacheable):
        return cls.initialize(pd.read_json(cacheable, orient='split'))

    @classmethod
    def from_parsed_to_data(cls, parsed):
        return cls.initialize(pd.DataFrame(parsed, columns=cls.parsed_columns_order))

    @classmethod
    def order_columns(cls, data):
        return data[cls.columns_order]

    def __init__(self, data):
        self.data = data

    @staticmethod
    def query_from(data, query):
        result = data
        for field, (matcher, required_values) in query.items():
            result = result[result[field].apply(lambda val: any([matcher(val, req_val) for req_val in required_values]))]
        return result

    @staticmethod
    def post_process(data):
        data = data.dropna(subset=[FOOD_NAME])
        return data

    @staticmethod
    def to_cacheable(data):
        return data.to_json(orient='split')

    @staticmethod
    def to_tabular(data):
        return data.to_dict('records')

    def get(self):
        return self.data

class Regs(Data):

    processed_data_path = PROCESSED_DATA
    parsed_columns_order = PARSER_COLUMNS_ORDER
    columns_order = [FILE, REG, WEEK, DAY_NAME, WEIGHT, MEAL_NUM, FOOD_NAME, AMOUNT, GRAMS]

    @staticmethod
    def initialize_types(data):
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

    @staticmethod
    def build():
        file_reg = read(HISTORIC_DATA)
        failed, regs = parse(file_reg)
        data = Regs.from_parsed_to_data(regs)
        return data

    @staticmethod
    def wrap_null_values(data):
        return data.fillna(0)

class Foods(Data):

    processed_data_path = DB_DATA
    columns_order = [FOOD_NAME, AMOUNT, CALS, PROTEIN, CARBS, FAT]

    @staticmethod
    def initialize_types(data):
        data[FOOD_NAME] = data[FOOD_NAME].astype('string')
        data[AMOUNT] = data[AMOUNT].astype('Float32')
        data[CALS] = data[CALS].astype('Float32')
        data[PROTEIN] = data[PROTEIN].astype('Float32')
        data[CARBS] = data[CARBS].astype('Float32')
        data[FAT] = data[FAT].astype('Float32')
        return data

    @staticmethod
    def build():
        dbs = {}

        def processor(f, dbs, identifier):
            dbs[identifier] = load(f)
            return dbs

        for path, identifier in LEGACY_METADATA:
            cacheable = open_and_process_file(path, processor, (dbs, identifier))

        return Foods.initialize(pd.DataFrame(cacheable).reset_index().rename(columns={'index': FOOD_NAME}))

    @staticmethod
    def wrap_null_values(data):
        return data.fillna(0)

    def get_all_food_names(self):
        return set(self.data[FOOD_NAME])
