from data_constants import SECONDS_IN_HOUR, SECONDS_IN_MINUTE, MINUTES_IN_HOUR

def round_weight(weight):
    return round(weight, 1)

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
