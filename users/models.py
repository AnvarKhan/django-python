from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	age = models.PositiveSmallIntegerField(null=True, blank=True)
	address = models.CharField(max_length=200)
	job = models.CharField(max_length=50)

