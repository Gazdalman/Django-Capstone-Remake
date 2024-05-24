from django.db import models
from projects.models import Project

# Create your models here.
class Reward(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(null=False, blank=False, max_length=50)
  amount = models.FloatField(null=False, blank=False)
  description = models.CharField(max_length=150)
  image = models.CharField(max_length=255)
  quantity = models.IntegerField()
  unlimited = models.BooleanField(default=False, null=False, blank=False)
  delivery_date = models.DateTimeField(null=False, blank=False)

class RewardItem(models.Model):
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
  title = models.CharField(max_length=50, null=False, blank=False)
  quantity = models.IntegerField(null=False, blank=False)
  image = models.CharField(max_length=255)
