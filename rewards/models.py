from django.db import models

# Create your models here.
class Reward(models.Model):
  title = models.CharField(null=False, blank=False, max_length=50)
  amount = models.FloatField(null=False, blank=False)
