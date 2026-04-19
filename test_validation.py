import unittest
from validation import validate_email, validate_password, validate_phone

class TestValidation(unittest.TestCase):

    # ================= EMAIL TEST =================
    def test_email_valid(self):
        self.assertEqual(validate_email("user@gmail.com"), "Valid")

    def test_email_no_at(self):
        self.assertNotEqual(validate_email("usergmail.com"), "Valid")

    def test_email_empty(self):
        self.assertNotEqual(validate_email(""), "Valid")

    def test_email_with_space(self):
        self.assertNotEqual(validate_email("user @gmail.com"), "Valid")
    
    def test_email_invalid_format(self):
        self.assertNotEqual(validate_email("user@gmail"), "Valid")


    # ================= PASSWORD TEST =================
    def test_password_valid(self):
        self.assertEqual(validate_password("Abcdef12"), "Valid")

    def test_password_short(self):
        self.assertNotEqual(validate_password("Abc12"), "Valid")

    def test_password_no_upper(self):
        self.assertNotEqual(validate_password("abcdef12"), "Valid")

    def test_password_no_lower(self):
        self.assertNotEqual(validate_password("ABCDEF12"), "Valid")

    def test_password_no_number(self):
        self.assertNotEqual(validate_password("Abcdefgh"), "Valid")
    
    def test_password_with_space(self):
        self.assertNotEqual(validate_password("Abc def12"), "Valid")


    # ================= PHONE TEST =================
    def test_phone_valid(self):
        self.assertEqual(validate_phone("081234567890"), "Valid")

    def test_phone_short(self):
        self.assertNotEqual(validate_phone("08123"), "Valid")

    def test_phone_letters(self):
        self.assertNotEqual(validate_phone("08123abcd"), "Valid")

    def test_phone_empty(self):
        self.assertNotEqual(validate_phone(""), "Valid")

    def test_phone_too_long(self):
        self.assertNotEqual(validate_phone("0812345678901234"), "Valid")

if __name__ == '__main__':
    unittest.main()