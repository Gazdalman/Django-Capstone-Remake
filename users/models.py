from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
  username = models.CharField(max_length=25, null=False, blank=False, unique=True)
  password = models.CharField(max_length=255, null=False, blank=False)
  email = models.EmailField(unique=True, null=False)
  first_name = models.CharField(max_length=250, null=False, blank=False)
  last_name = models.CharField(max_length=250, null=False, blank=False)

  def __str__(self):
    return self.username

  def to_dict(self):
    return {
      "username": self.username,
      "email": self.email,
      "firstName": self.first_name,
      "lastName": self.last_name
    }
