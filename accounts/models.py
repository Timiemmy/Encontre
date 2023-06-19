from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
