from django.db import models
from projects.models import Project

# Create your models here.
class Reward(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')
  title = models.CharField(null=False, blank=False, max_length=50)
  amount = models.FloatField(null=False, blank=False)
  description = models.CharField(max_length=150)
  image = models.CharField(max_length=255)
  quantity = models.IntegerField()
  unlimited = models.BooleanField(default=False, null=False, blank=False)
  delivery_date = models.DateTimeField(null=False, blank=False)

  def __str__(self):
    return f'{self.title}: Project {self.project.id}'

  def to_dict(self):
    return {
      "id": self.id,
      "projectId": self.project_id,
      "image": self.image,
      "title": self.title,
      "description": self.description,
      "shipping": self.shipping,
      "physicalItems": self.physical_items,
      "amount": self.amount,
      "unlimited": self.unlimited,
      "quantity": self.quantity,
      "deliveryDate": self.delivery_date,
    }

class RewardItem(models.Model):
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='items')
  title = models.CharField(max_length=50, null=False, blank=False)
  quantity = models.IntegerField(null=False, blank=False)
  image = models.CharField(max_length=255)

  def to_dict(self):
    return {
      "id": self.id,
      "rewardId": self.reward_id,
      "title": self.title,
      "image": self.image,
      "quantity": self.quantity
    }
