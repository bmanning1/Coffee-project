from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms


class CustomUserTest(TestCase):
    """ Creating some tests for the User """

    def test_manager_create(self):
        """ Test User creation """
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    def test_registration_form(self):
        # Test Registration
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'password',
            'password2': 'password',
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        # Test Registration with missing email
        form = UserRegistrationForm({
            'password1': 'password',
            'password2': 'password',
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())
