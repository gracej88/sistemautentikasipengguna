import unittest
from user_service import register_user

class TestIntegration(unittest.TestCase):

    def test_register_success(self):
        result = register_user("user@gmail.com", "Abcdef12", "081234567890")
        self.assertEqual(result, "User registered successfully")

    def test_register_invalid_email(self):
        result = register_user("usergmail.com", "Abcdef12", "081234567890")
        self.assertEqual(result, "Email tidak valid")

    def test_register_invalid_password(self):
        result = register_user("user@gmail.com", "abc", "081234567890")
        self.assertEqual(result, "Password tidak valid")

    def test_register_invalid_phone(self):
        result = register_user("user@gmail.com", "Abcdef12", "08abc")
        self.assertEqual(result, "Nomor telepon tidak valid")

    def test_register_empty_data(self):
        result = register_user("", "", "")
        self.assertEqual(result, "Email tidak valid")


if __name__ == "__main__":
    unittest.main()