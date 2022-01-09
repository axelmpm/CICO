from re import search

def get_indexes_of(element, sequence, exact_match=True):
    if exact_match:
        def filter(e, element):
            return element == e
    else:
        def filter(e, element):
            return element in e
    return [i for i, e in enumerate(sequence) if filter(e, element)]

def flatten(sequence):
    flattened = []
    for e in sequence:
        if type(e) is list:
            flattened.extend(flatten(e))
        else:
            flattened.append(e)
    return flattened

def tuple_flatten(elements):
    flattened = []
    if type(elements) is list:
        return [tuple_flatten(e) for e in elements]
    elif type(elements) is tuple:
        for e in elements:
            if type(e) is tuple:
                flattened.extend(list(tuple_flatten(e)))
            else:
                flattened.append(e)
        return tuple(flattened)
    else:
        return elements

def distribute(x, y):
    if type(y) is list:
        return [distribute(x, e) for e in y]
    elif type(y) is tuple:
        return tuple([x] + list(y))
    else:
        return (x, y)

def collapse(structure):
    if type(structure) is list:
        return flatten([collapse(e) for e in structure])
    if type(structure) is tuple:
        x, s = structure[:-1], structure[-1]
        return tuple_flatten(distribute(x, collapse(s)))
    else:
        return structure

def split_into_classes(sequence, mapper):
    classes = {}
    for e in sequence:
        if mapper(e) in classes:
            classes[mapper(e)].append(e)
        else:
            classes[mapper(e)] = [e]
    return classes

def my_search(pattern, target, string):
    matches = search(pattern, string)
    if matches:
        for match in matches.groups():
            if match is not None and search(target, match):
                return match
    return None

def matches_with(patterns, target, string):
    for pattern in patterns:
        if match := my_search(pattern, target, string):
            return match
    return None
