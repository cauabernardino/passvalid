"""
Functions to the Password Validator

Considerations:
1) Tuples always have length == 3
2) Maximum of 4 requirements
"""
import string

special_chars = string.punctuation


def comparisons(act_integer, operation, req_integer):
    """
    Handles the comparisons between the requirements and password params.
    The operations (str) are: <, >, =
    """

    if operation == '<':
        return act_integer < req_integer
    elif operation == '>':
        return act_integer > req_integer
    else:
        return act_integer == req_integer     


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

    return comparisons(len(password), operation, integer)     


def validate_letters(password, operation, integer):
    """Validates the quantity of letters in password"""
    qty = 0

    for letter in password:
        if letter.isalpha():
            qty += 1
    
    return comparisons(qty, operation, integer) 


def validate_numbers(password, operation, integer):
    """"Validates the quantity of numbers in password"""
    qty = 0

    for number in password:
        if number.isnumeric():
            qty += 1

    return comparisons(qty, operation, integer) 


def validate_specials(password, operation, integer):
    """Validates the quantity of special characters"""
    qty = 0

    for special in password:
        if special in special_chars:
            qty += 1

    return comparisons(qty, operation, integer) 
