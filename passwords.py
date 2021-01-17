from passvalid.validator import validator


if __name__ == '__main__':
    password = input('Define password: ')

    req1 = [
        ('LEN', '>', 8),
        ('NUMBERS', '<', 10),
        ('LETTERS', '>',  5),
        ('SPECIALS', '=', 3)
    ]

    req2 = [
        ('SPECIALS', '>', 1),
        ('LEN', '>', 5),
        ('NUMBERS', '=', 2)
    ]

    print(validator(password, req1))