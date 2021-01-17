"""
Password Validator

Considerations:
1) Only native Python modules used
2) Tuples always have length == 3
3) Minimum of 1 and maximum of 4 requirements
"""
from passvalid import functions


## Output text
valid_text = "VALID. The password matches the requirements."
error_len = "INVALID. Length does not match the requirements."
error_letters = "INVALID. Quantity of letters does not match the requirements."
error_numbers = "INVALID. Quantity of numbers does not match the requirements."
error_specials = "INVALID. Quantity of specials characters does not match the requirements."


def validator(password, req):
    """
    Validates the password with given requirements
    Inputs:
    - Password
    - List of tuples with requirements. Ex: [('NUMBERS', ‘<’, 10), (‘SPECIALS’, ‘=’, 2)]
    - Requirements can be: LEN, LETTERS, NUMBERS, SPECIALS
    - Operations can be: <, > and =
    """
    if len(req) == 0:
        return "No requirements inputted."


    requirements, operations, integers = functions.split_req(req)

    for i in range(len(requirements)):
        if requirements[i] == 'LEN':
            len_is_valid = functions.validate_len(password, operations[i], integers[i])
            if not len_is_valid:
                return error_len
        elif requirements[i] == 'LETTERS':
            letters_is_valid = functions.validate_letters(password, operations[i], integers[i])
            if not letters_is_valid:
                return error_letters
        elif requirements[i] == 'NUMBERS':
            numbers_is_valid = functions.validate_numbers(password, operations[i], integers[i])
            if not numbers_is_valid:
                return error_numbers
        elif requirements[i] == 'SPECIALS':
            specials_is_valid = functions.validate_specials(password, operations[i], integers[i])
            if not specials_is_valid:
                return error_specials
    
    return valid_text
