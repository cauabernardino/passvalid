# Password Validator

Password Validator module that validates passwords with the given requirements.

It goes through each requirement in order and stops in the first one that does not match or when it validates all of them.

Made with native Python modules only.

## Example

1. You can run the `passwords.py` file for an example with:
```bash
# Windows
python passwords.py

# Linux
python3 passwords.py 
```
## How to run

1. **Import the validator**
```python
from passvalid.validator import validator
```

2. **Set the requirements. They must be a list of tuples with the following format:**
```python
requirements = [
    ('LEN', '>', 8),
    ('NUMBERS', '<', 10),
    ('LETTERS', '>',  5),
    ('SPECIALS', '=', 3)
]
```
Where:
 - First value:

     - LEN – password length
     - LETTERS – # of letters
     - NUMBERS – # of numbers1
     - SPECIALS – # of special characters

- Second value: <, > or =

- Third value: an integer number

3. **Call it with the password and requirements**
```python
print(validator(password, requirements))
```

4. It returns a INFO message and the status of the password (Valid or Invalid):
```bash
# Using the requirements shown in Step 2

# Example of valid password
password = 'tests123a*)!'

INFO: The password matches the requirements.
VALID PASSWORD.


# Example of invalid password
password = 'tests123'

INFO: Length does not match the requirements.
INVALID PASSWORD.
```

## Testing

1. Set the test parameters in `test_parameters.py`
2. Run the tests with
```bash
# Windows
python tests.py -v

# Linux
python3 tests.py -v
```