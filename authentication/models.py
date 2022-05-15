from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")

    EMAIL_FIELD: str = "email"
    USERNAME_FIELD: str = "username"
