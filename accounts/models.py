from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phoneNumber = models.CharField(max_length=15, unique=True)

    REQUIRED_FIELDS = ["first_name", "last_name", "phoneNumber"]

    def __str__(self):
        return self.username
