## Password for Testing
pw1 = 'password25!*'
pw2 = '!*passw0rd10@'


## Parameters for test_equal 
req1_equal = [
    ('LEN', '=', 12),
    ('SPECIALS', '=', 2)
]

req2_equal = [
    ('NUMBERS', '=', 3),
    ('LETTERS', '=',  5),
]


## Parameters for test_greater
req1_greater = [
    ('LEN', '>', 10),
    ('SPECIALS', '>', 1)
]

req2_greater = [
    ('NUMBERS', '>', 4),
    ('LETTERS', '>',  5),
]


## Parameter for test_less
req1_less = [
    ('NUMBERS', '<', 10),
    ('LEN', '<', 20)
]

req2_less = [
    ('SPECIALS', '<', 3),
    ('LETTERS', '<',  10),
]