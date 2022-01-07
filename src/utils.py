
def get_indexes_of(element, sequence, containing=False):
    if containing:
        def filter(e, element):
            return element in e
    else:
        def filter(e, element):
            return element == e
    return [i for i, e in enumerate(sequence) if filter(e, element)]

def flatten(sequence):
    flattened = []
    for e in sequence:
        if type(e) is list:
            flattened.extend(flatten(e))
        else:
            flattened.append(e)
    return flattened

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
    if type(structure) is tuple and len(structure) == 2:
        x, s = structure
        return distribute(x, collapse(s))
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
