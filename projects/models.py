from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from users.models import User
from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.dispatch import receiver
from django.utils import timezone
from util import remove_file_from_s3

# Create your models here.
class Project(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=60, null=False, blank=False)
  subtitle = models.CharField(max_length=135, null=False, blank=False)
  location = models.CharField(max_length=50, null=False, blank=False)
  image = models.CharField(max_length=550, null=False, blank=False)
  video = models.CharField(max_length=550, null=False, blank=False)
  type = models.CharField(max_length=50, null=False, blank=False)
  goal = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)])
  main_category = models.CharField(max_length=50, null=False, blank=False)
  main_subcat = models.CharField(max_length=50, null=False, blank=False)
  second_cat = models.CharField(max_length=50)
  second_subcat = models.CharField(max_length=50)
  launch_date = models.DateTimeField(null=False, blank=False)
  end_date = models.DateTimeField(null=False, blank=False)
  launched = models.BooleanField(default=False)
  earned_today = models.FloatField(default=0)

  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.user,
      "title": self.title,
      "subtitle": self.subtitle,
      "location": self.location,
      "type": self.type,
      "image": self.image,
      "video": self.video,
      "goal": self.goal,
      "launchDate": self.launch_date,
      "endDate": self.end_date,
      "story": [story.to_dict() for story in self.story][0] if self.story else "",
      "mainCategory": self.main_category,
      "mainSub": self.main_subcat,
      "secondCat": self.second_cat if self.second_cat else '',
      "secondSub": self.second_subcat if self.second_subcat else '',
      "rewards": sorted([reward.to_dict() for reward in self.rewards], key=lambda reward : reward['amount']),
      "launched": self.launch_date <= datetime.now(),
      "user": self.user.display_name,
      "earned": sum([backer.amount for backer in self.backers]),
      "earnedToday": self.earned_today,
    }

  def __str__(self):
    return self.title


# @receiver(models.signals.pre_delete, sender=Project)
# def on_project_delete(sender, instance, **kwargs):
#   remove_file_from_s3(instance.image)
#   if instance.video:
#     remove_file_from_s3(instance.video)


def reset_earned_today():
  with transaction.atomic():
    projects = Project.objects.all()
    for project in projects:
      project.earned_today = 0
      project.save()


def check_if_launched():
  with transaction.atomic():
    projects = Project.objects.all()
    for project in projects:
      if project.launch_date <= timezone.now():
        project.launched = True
      else:
        project.launched = False
      project.save()

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
  reset_earned_today,
  'cron',
  hour=5
)

scheduler.add_job(
  check_if_launched,
  'cron',
  hour=5
)

class Like(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

  def to_dict(self):
    return {
      "userId": self.user_id,
      "projectId": self.project_id,
    }

class Story(models.Model):
  project_id = models.OneToOneField(Project, on_delete=models.CASCADE)
  title = models.CharField(max_length=60, null=False, blank=False)
  content = models.TextField(null=False, blank=False)

  def to_dict(self):
    return {
      "title": self.title,
      "content": self.content,
    }
