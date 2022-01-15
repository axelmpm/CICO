WEEK_SYMBOL = 'Semana'

DIVIDER = '---'
INTERLINE_SEPARATOR = '\n'
WEIGHT_KEYWORD = 'PESO'

INTEGER_PATTERN = '-?[0-9]+'
FLOAT_PATTERN = '-?[0-9]+\\.[0-9]+'
NUMBER_PATTERN = '-?[0-9]+\\.?[0-9]*'
WEIGHT_PATTERN = f'{WEIGHT_KEYWORD}\\s*:?'
FOOD_NAME_PATTERN = '([a-zA-Z]{2,}\\s*)+'

DAYS_ORDER = {
    'Lunes': 0,
    'Martes': 1,
    'Miercoles': 2,
    'Miércoles': 2,
    'Jueves': 3,
    'Viernes': 4,
    'Sabado': 5,
    'Sábado': 5,
    'Domingo': 6,
}

DAYS_NAMES = list(DAYS_ORDER.keys())
