import unittest
import passvalid.validator as pv

from test_parameters import *


class TestValidator(unittest.TestCase):
    """Tests the operations for Password Validator module"""
    def test_equal_valid(self):
        self.assertEqual(pv.validator(pw1, req1_equal), pv.valid_password)

    def test_equal_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_equal), pv.invalid_password)

    def test_greater_valid(self):
        self.assertEqual(pv.validator(pw1, req1_greater), pv.valid_password)

    def test_greater_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_greater), pv.invalid_password)

    def test_less_valid(self):
        self.assertEqual(pv.validator(pw1, req1_less), pv.valid_password)
    
    def test_less_invalid(self):
        self.assertEqual(pv.validator(pw2, req2_less), pv.invalid_password)
    

if __name__ == '__main__':
    unittest.main()