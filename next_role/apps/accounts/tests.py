from django.test import TestCase

# Create your tests here.


from django.test import TestCase

from apps.accounts.models import User
from apps.accounts.services.auth_service import register_user




class RegistrationTest(TestCase):
    def setUp(self):
        # This runs before every test method
        self.base_data = {
            "email": "candidate@example.com",
            "username": "candidate_user",
            "password": "SecurePassword123!",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "08011112222",
        }

    def test_register_candidate_success(self):
        """Test that a user can register with the default candidate role"""
        user = register_user(self.base_data)

        self.assertEqual(user.email, "candidate@example.com")
        self.assertEqual(user.role, User.Role.CANDIDATE)
        # Verify password is NOT stored in plain text
        self.assertNotEqual(user.password, "SecurePassword123!")
        self.assertTrue(user.check_password("SecurePassword123!"))

    def test_register_employer_success(self):
        """Test that a user can register explicitly as an employer"""
        data = self.base_data.copy()
        data["email"] = "employer@example.com"
        data["username"] = "employer_user"
        data["role"] = User.Role.EMPLOYER

        user = register_user(data)

        self.assertEqual(user.role, User.Role.EMPLOYER)
        self.assertEqual(user.email, "employer@example.com")

    def test_duplicate_email_fails(self):
        """Test that registering with an existing email raises an error"""
        register_user(self.base_data)

        with self.assertRaises(Exception):
            # Try to register the same data again
            register_user(self.base_data)
