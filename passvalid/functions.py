"""
Functions to the Password Validator

Considerations:
1) Tuples always have length == 3
2) Maximum of 4 requirements
"""
import string

special_chars = string.punctuation


def split_req(requirements):
    """Separate the requirements, operation and integers from the tuples"""
    reqs = []
    operations = []
    integers = []

    for values in requirements:
        reqs.append(values[0])
        operations.append(values[1])
        integers.append(values[2])

    return reqs, operations, integers


def validate_len(password, operation, integer):
    """Validates the password's length"""
    if operation == '<':
        return len(password) < integer
    elif operation == '>':
        return len(password) > integer
    else:
        return len(password) == integer       


def validate_letters(password, operation, integer):
    """Validates the quantity of letters in password"""
    qty = 0

    for letter in password:
        if letter.isalpha():
            qty += 1
    
    if operation == '<':
        return qty < integer
    elif operation == '>':
        return qty > integer
    else:
        return qty == integer


def validate_numbers(password, operation, integer):
    """"Validates the quantity of numbers in password"""
    qty = 0

    for number in password:
        if number.isnumeric():
            qty += 1

    if operation == '<':
        return qty < integer
    elif operation == '>':
        return qty > integer
    else:
        return qty == integer


def validate_specials(password, operation, integer):
    """Validates the quantity of special characters"""
    qty = 0

    for special in password:
        if special in special_chars:
            qty += 1

    if operation == '<':
        return qty < integer
    elif operation == '>':
        return qty > integer
    else:
        return qty == integer
