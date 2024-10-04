from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('superuser', 'Super User'),
        ('admin', 'Admin User'),
        ('user', 'General User'),
    ]
    
    email = models.EmailField(_("Email"),unique=True)
    role = models.CharField(max_length=126, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(_("Is this user active ?"), default=True)
    is_staff = models.BooleanField(_("Is this user staff ?"), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email