import unittest
from pycpfcnpj import cnpj


class CNPJTests(unittest.TestCase):
    """docstring for CNPJTests"""

    def setUp(self):
        self.valid_cnpj = "11444777000161"
        self.masked_valid_cnpj = "11.444.777/0001-61"
        self.invalid_cnpj = "11444777000162"
        self.masked_invalid_cnpj = "11.444.777/0001-62"
        self.invalid_cnpj_whitespaces = "11444 777000161"
        self.invalid_cnpj_with_alphabetic = "11444d777000161"

    def test_validate_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.valid_cnpj))

    def test_validate_masked_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.masked_valid_cnpj))

    def test_validate_cnpj_false(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj))

    def test_validate_masked_cnpj_false(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj))

    def test_validate_cnpj_with_same_numbers(self):
        for i in range(10):
            self.assertFalse(cnpj.validate("{0}".format(i) * 14))

    def test_validate_cnpj_with_whitespaces(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj_whitespaces))

    def test_validate_cnpj_with_alphabetic_characters(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj_with_alphabetic))


if __name__ == "__main__":
    unittest.main(verbosity=2)
