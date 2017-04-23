from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms


class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)


class CustomUserTest(TestCase):
    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())
