from django.db import models
from projects.models import Project
from rewards.models import Reward
from users.models import User

# Create your models here.
class Backer(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backed')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='backers')
  amount = models.FloatField(null=False, blank=False)
  rewards = models.ManyToManyField(Reward, through='BackerReward', related_name='backers')

  def to_dict(self):
    return {
      'id': self.id,
      'userId': self.user.id,
      'amount': self.amount,
      'rewards': [reward.to_dict() for reward in self.rewards]
    }

class BackerReward(models.Model):
  backer = models.ForeignKey(Backer, on_delete=models.CASCADE)
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE)

  def __str__(self):
        return f"{self.backer} - {self.reward}"
