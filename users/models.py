from django.contrib.auth.models import AbstractUser
from django.db import models


class RestUser(AbstractUser):

    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=18)
