from json import load
from enum import Enum

from src.reader.reader import read, new_regs_exist_at, open_and_process_file
from src.parser.parser_main import parse
from src.processor.processor_lib import read_regs_db_from, read_foods_db_from, food_json_db_into_data, into_data
from src.paths import PROCESSED_DATA, HISTORIC_DATA, DB_DATA, LEGACY_METADATA

def read_all(dirs):
    return sum([read(dir) for dir in dirs], [])

def read_and_parse(dirs):
    file_reg = read_all(dirs)
    failed, regs = parse(file_reg)
    return failed, regs

def read_parse_process_regs_db(dirs):
    failed, regs = read_and_parse(dirs)
    data = into_data(regs)
    return data

def read_and_parse_legacy_foods_dbs(paths_metadata):
    dbs = {}

    def processor(f, dbs, identifier):
        dbs[identifier] = load(f)
        return dbs

    for path, identifier in paths_metadata:
        dbs = open_and_process_file(path, processor, (dbs, identifier))

    return food_json_db_into_data(dbs)

def store(db, path):
    db.to_csv(path)

def basic_load(path, alternative, reader, parser):
    try:
        data = reader(path)
    except FileNotFoundError:
        data = parser(alternative)
        store(data, path)
    return data

class DBType(Enum):
    REGS = 1
    FOODS = 2

class DBMetadata(Enum):
    LOAD_PATH = 1
    PARSE_PATH = 2
    READER = 3
    PARSER = 4

loader = {
    DBType.REGS: {
        DBMetadata.LOAD_PATH: PROCESSED_DATA,
        DBMetadata.PARSE_PATH: [HISTORIC_DATA],
        DBMetadata.READER: read_regs_db_from,
        DBMetadata.PARSER: read_parse_process_regs_db},
    DBType.FOODS: {
        DBMetadata.LOAD_PATH: DB_DATA,
        DBMetadata.PARSE_PATH: LEGACY_METADATA,
        DBMetadata.READER: read_foods_db_from,
        DBMetadata.PARSER: read_and_parse_legacy_foods_dbs},
}

def load_regs_db():
    return basic_load(
        loader[DBType.REGS][DBMetadata.LOAD_PATH],
        loader[DBType.REGS][DBMetadata.PARSE_PATH],
        loader[DBType.REGS][DBMetadata.READER],
        loader[DBType.REGS][DBMetadata.PARSER])

def load_foods_db():
    return basic_load(
        loader[DBType.FOODS][DBMetadata.LOAD_PATH],
        loader[DBType.FOODS][DBMetadata.PARSE_PATH],
        loader[DBType.FOODS][DBMetadata.READER],
        loader[DBType.FOODS][DBMetadata.PARSER])
