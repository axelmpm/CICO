
FIELD_PARSERS = []
def parse_food_grams(raw_reg):
    pass

def parse_food_amount(raw_reg):
    pass

def parse_food_carbs(raw_reg):
    pass

def parse_food_fat(raw_reg):
    pass

def parse_food_protein(raw_reg):
    pass

def parse_food_name(raw_reg):
    pass

def parse_reg(raw_reg):
    fields = []
    for field_identifier, field_parser in FIELD_PARSERS:
        raw_reg, field = field_parser(raw_reg)
        fields.append((field_identifier, field))
    return fields
