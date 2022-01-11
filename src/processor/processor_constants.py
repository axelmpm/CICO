import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

from src.parser.parser_fields import ORDERED_FIELDS, VISIBLE_FIELDS, AGGREGABLE_FIELDS

MICROSECONDS_IN_SECOND = 10**6
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = SECONDS_IN_HOUR / SECONDS_IN_MINUTE

FILE = 'file'
WEEK = 'week'
DAY_NAME = 'day_name'
WEIGHT = 'weight'
MEAL_NUM = 'meal_num'
FIELD_KEY = 'field_key'
FIELD_VALUE = 'field_value'

ORDERED_NO_FIELDS_COLUMNS = [FILE, WEEK, DAY_NAME, WEIGHT, MEAL_NUM]
READABLE_COLUMNS = ORDERED_NO_FIELDS_COLUMNS + ORDERED_FIELDS
VISIBLE_COLUMNS = [WEEK, DAY_NAME, WEIGHT] + VISIBLE_FIELDS
