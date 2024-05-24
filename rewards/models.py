from django.db import models
from projects.models import Project

# Create your models here.
class Reward(models.Model):
  project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(null=False, blank=False, max_length=50)
  amount = models.FloatField(null=False, blank=False)
  description = models.CharField(max_length=150)
  image = models.CharField(max_length=255)
  quantity = models.IntegerField()
  unlimited = models.BooleanField(default=False, null=False, blank=False)
  delivery_date = models.DateTimeField(null=False, blank=False)
  