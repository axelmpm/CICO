def base_atomic_parsing(raw, checker, parser, error_message, raises=True):
    if metadata := checker(raw):
        return parser(metadata, raw)
    else:
        raise SyntaxError(f'{error_message}: {raw}') if raises else None

def is_valid(something):
    pass  # TODO
