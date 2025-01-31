from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
