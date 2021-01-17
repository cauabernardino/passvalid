## Passwords for Testing
pw1 = 'password25!*'
pw2 = '!*passw0rd10@'


"""
Parameters for equal tests (test_equal)
""" 
# This requirement should be valid for the password pw1
req1_equal = [
    ('LEN', '=', 12),
    ('SPECIALS', '=', 2)
]

# This requirement should be invalid for the password pw2
req2_equal = [
    ('NUMBERS', '=', 3),
    ('LETTERS', '=',  5),
]


"""
Parameters for greater than tests (test_greater)
""" 
# This requirement should be valid for the password pw1
req1_greater = [
    ('LEN', '>', 10),
    ('SPECIALS', '>', 1)
]
# This requirement should be invalid for the password pw2
req2_greater = [
    ('NUMBERS', '>', 4),
    ('LETTERS', '>',  5),
]

"""
Parameters for less than tests (test_greater)
""" 
# This requirement should be valid for the password pw1
req1_less = [
    ('NUMBERS', '<', 10),
    ('LEN', '<', 20)
]

# This requirement should be invalid for the password pw2
req2_less = [
    ('SPECIALS', '<', 3),
    ('LETTERS', '<',  10),
]