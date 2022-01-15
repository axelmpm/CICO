from datetime import timedelta

from data_constants import SECONDS_IN_HOUR, SECONDS_IN_MINUTE, MINUTES_IN_HOUR, DAYS_IN_WEEK
from data_constants import FOOD_NAME, AMOUNT, AMOUNT_GRAMS, GRAMS, WEEK, DATE
from src.data.data_constants import BUILDABLE_FIELDS, AGGREAGABLE_FIELDS
from src.parser.parser_constants import DAYS_ORDER

def round_weight(f):
    return round(f, 1)

def round_float(f):
    return round(f, 1)

def to_hours(timedelta):
    return timedelta.total_seconds() / SECONDS_IN_HOUR

def to_minutes(timedelta):
    return timedelta.total_seconds() / SECONDS_IN_MINUTE

def to_formated_duration(timedelta):
    total_hours = to_hours(timedelta)
    hours = int(total_hours)
    minutes = int((total_hours - hours) * MINUTES_IN_HOUR)
    return f"{hours} hs, {minutes} mins"

def eq(val1, val2):
    return val1 == val2

def close_to(val1, val2, precision):
    return abs(val1 - val2) <= precision

def ge(val1, val2):
    return val1 >= val2

def le(val1, val2):
    return val1 <= val2

def gt(val1, val2):
    return val1 > val2

def lt(val1, val2):
    return val1 < val2

def contains(val1, val2):
    return val2 in val1

def build_field(field, grams, amount, amount_grams):
    if grams == 0:
        grams = amount * amount_grams
    return grams * field

def merge(regs, foods):
    regs = regs.get()
    foods = foods.get()
    data_merge = regs.merge(foods, on=[FOOD_NAME], how='inner')

    for field in BUILDABLE_FIELDS:
        data_merge[field] = data_merge.apply(lambda r: build_field(r[field], r[GRAMS], r[AMOUNT], r[AMOUNT_GRAMS]), axis=1)

    return data_merge

def group_and_aggregate_by(data, key_cols, val_cols):
    return data.groupby(key_cols)[val_cols].sum().reset_index()

def group_and_aggregate_by_days(regs, foods):
    return group_and_aggregate_by(merge(regs, foods), [DATE], AGGREAGABLE_FIELDS)

def group_and_aggregate_by_weeks(regs, foods):
    return group_and_aggregate_by(merge(regs, foods), [WEEK], AGGREAGABLE_FIELDS)

def build_date(base_date, week, day_name):
    days = ((week - 1) * DAYS_IN_WEEK) + DAYS_ORDER[day_name]
    return base_date + timedelta(days=days)

def tail(data, key_columns, amount):
    return data[data[key_columns].isin(data[key_columns].drop_duplicates().sort_values().tail(amount))]

def amount_grams_to_visual(amount_grams):
    return 100 if amount_grams == 0 else amount_grams

def date_to_string(datetm):
    return datetm.strftime('%Y-%m-%d')
