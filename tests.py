import unittest
import passvalid.validator as pv

from test_parameters import *


class TestValidator(unittest.TestCase):
    """Tests the operations for Password Validator module"""
    def test_equal_valid(self):
        self.assertEqual(pv.validator(pw1, req1_equal), pv.valid_text)

    def test_equal_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_equal), pv.error_letters)

    def test_greater_valid(self):
        self.assertEqual(pv.validator(pw1, req1_greater), pv.valid_text)

    def test_greater_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_greater), pv.error_numbers)

    def test_less_valid(self):
        self.assertEqual(pv.validator(pw1, req1_less), pv.valid_text)
    
    def test_less_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_less), pv.error_specials)
    


if __name__ == '__main__':
    unittest.main()