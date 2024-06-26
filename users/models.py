from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
  username = models.CharField(max_length=25, null=False, blank=False, unique=True)
  password = models.CharField(max_length=255, null=False, blank=False)

  def __str__(self):
    return self.username
