from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


class AccountUserManager(UserManager):
    def _create_user(self, username, first_name, last_name, email, password,
                     is_staff, is_superuser, **extra_fields):
        # Creates and saves a User with the given username, email and password
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email, first_name=first_name, last_name=last_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    objects = AccountUserManager()
    # Is the User Subscribed?
    def is_subscribed(self, coffee):
        try:
            purchase = self.purchases.get(coffee__pk=coffee.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True
