
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

def contained_in(val1, val2):
    return val1 in val2


def query_from(db, query):
    """
    query := {
        field_1: [value_11, value_12, ..., value_1n],
        .
        .
        .
        field_m: [value_m1, value_m2, ..., value_mn]
        }
    returns all the regs that satisfies to have one of the values asociated with the its field for every field
    """
    result = db
    for field, (matcher, required_values) in query.items():
        result = result[result[field].apply(lambda val: any([matcher(val, req_val) for req_val in required_values]))]
    return result
