from enum import Enum

from parser_utils import base_atomic_parsing

class FieldIdentifier(Enum):
    GRAMS = 1
    CALS = 2
    AMOUNT = 3
    CARBS = 4
    FAT = 5
    PROTEIN = 6
    WATER = 7
    FOOD_NAME = 8
    SALT = 9
    FIBER = 10
    GLYCEMIC_INDEX = 11
    QUALITY = 12

def parse_food_grams(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_cals(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_amount(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_carbs(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_fat(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_protein(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_name(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

def parse_food_quality(raw_reg):

    def checker(raw_reg):
        return raw_reg

    def parser(matched, raw_reg):
        return raw_reg

    error_message = ''
    return base_atomic_parsing(raw_reg, checker, parser, error_message, raises=False)

FIELD_PARSERS = [
    (FieldIdentifier.GRAMS, parse_food_grams),
    (FieldIdentifier.CALS, parse_food_cals),
    (FieldIdentifier.AMOUNT, parse_food_amount),
    (FieldIdentifier.CARBS, parse_food_carbs),
    (FieldIdentifier.FAT, parse_food_fat),
    (FieldIdentifier.PROTEIN, parse_food_protein),
    (FieldIdentifier.FOOD_NAME, parse_food_name),
    (FieldIdentifier.QUALITY, parse_food_quality),
]

def parse_reg(raw_reg):
    return [(field_identifier, field_parser(raw_reg)) for field_identifier, field_parser in FIELD_PARSERS]
