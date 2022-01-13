from src.reader.reader import compose_dir, compose_file_path
from src.database.fields_constants import AMOUNT, CALS, PROTEIN, CARBS, FAT, ALIASES

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

LEGACY_AMOUNT_DB_METADATA = (LEGACY_AMOUNT_DB_PATH, AMOUNT)
LEGACY_CALS_DB_METADATA = (LEGACY_CALS_DB_PATH, CALS)
LEGACY_PROTEIN_DB_METADATA = (LEGACY_PROTEIN_DB_PATH, PROTEIN)
LEGACY_CARBS_DB_METADATA = (LEGACY_CARBS_DB_PATH, CARBS)
LEGACY_FAT_DB_METADATA = (LEGACY_FAT_DB_PATH, FAT)
LEGACY_ALIASES_DB_METADATA = (LEGACY_ALIASES_DB_PATH, ALIASES)

LEGACY_METADATA = [
    LEGACY_AMOUNT_DB_METADATA, LEGACY_CALS_DB_METADATA,
    LEGACY_PROTEIN_DB_METADATA, LEGACY_CARBS_DB_METADATA, LEGACY_FAT_DB_METADATA]
