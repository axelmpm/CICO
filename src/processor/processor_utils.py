from processor_constants import SECONDS_IN_HOUR, SECONDS_IN_MINUTE, MINUTES_IN_HOUR

def to_hours(timedelta):
    return timedelta.total_seconds() / SECONDS_IN_HOUR

def to_minutes(timedelta):
    return timedelta.total_seconds() / SECONDS_IN_MINUTE

def to_formated_duration(timedelta):
    total_hours = to_hours(timedelta)
    hours = int(total_hours)
    minutes = int((total_hours - hours) * MINUTES_IN_HOUR)
    return f"{hours} hs, {minutes} mins"

def round_weight(weight):
    return round(weight, 1)
