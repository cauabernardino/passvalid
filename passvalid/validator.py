"""
Password Validator

Considerations:
1) Only native Python modules used
2) Tuples always have length == 3
3) Minimum of 1 and maximum of 4 requirements
"""
from passvalid import functions


## Output text
valid_password = "VALID PASSWORD."
invalid_password = "INVALID PASSWORD."
valid_text = "The password matches the requirements."
error_len = "Length does not match the requirements."
error_letters = "Quantity of letters does not match the requirements."
error_numbers = "Quantity of numbers does not match the requirements."
error_specials = "Quantity of specials characters does not match the requirements."


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
                print(f"INFO: {error_len}")
                return invalid_password

        elif requirements[i] == 'LETTERS':
            letters_is_valid = functions.validate_letters(password, operations[i], integers[i])

            if not letters_is_valid:
                print(f"INFO: {error_letters}")
                return invalid_password

        elif requirements[i] == 'NUMBERS':
            numbers_is_valid = functions.validate_numbers(password, operations[i], integers[i])

            if not numbers_is_valid:
                print(f"INFO: {error_numbers}")
                return invalid_password

        elif requirements[i] == 'SPECIALS':
            specials_is_valid = functions.validate_specials(password, operations[i], integers[i])

            if not specials_is_valid:
                print(f"INFO: {error_specials}")
                return invalid_password
    
    print(f"INFO: {valid_text}")
    return valid_password
