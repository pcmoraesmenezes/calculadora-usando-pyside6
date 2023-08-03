import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')  # Evita que ele encontre mais de um
#  caracter


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str):
    return len(string) == 0


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        return valid
    return valid
