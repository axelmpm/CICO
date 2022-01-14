from src.reader.reader import compose_dir, compose_file_path

BASE = 'C:/Users/axelpm/Desktop/cico'
TEST_DATA_DIR = compose_dir(BASE, 'test_data')
TEST_DATA_DIR_MEDIUM = compose_dir(BASE, 'test_data/medium')
TEST_DATA_DIR_LARGE = compose_dir(BASE, 'test_data/large')

PROCESSED_DATA = compose_file_path(BASE, 'under_testing_data.csv')  # TODO change
DB_DATA = compose_file_path(BASE, 'dbs/db.csv')
LEGACY_DB_DATA = compose_dir(BASE, 'dbs/legacy')
REAL_TIME_DATA = compose_dir(BASE, 'test_data/real_time_test_data')  # TODO change
HISTORIC_DATA = TEST_DATA_DIR

LEGACY_AMOUNT_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'amount_weight.json')
LEGACY_CALS_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'cal_facts.json')
LEGACY_PROTEIN_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'prot_facts.json')
LEGACY_CARBS_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'carb_facts.json')
LEGACY_FAT_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'fat_facts.json')
LEGACY_ALIASES_DB_PATH = compose_file_path(LEGACY_DB_DATA, 'aliases.json')
