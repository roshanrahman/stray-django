from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager

ACCOUNT_TYPE_CHOICES = (
    ('citizen', 'Citizen'),
    ('authority', 'Authority')
)


class CustomUser(AbstractUser):
    username = None
    phone = models.CharField(_('phone number'), max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    account_type = models.CharField(
        max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['account_type']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
