from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *

# Create your views here.
def home(request):
  # projects = Project.objects.filter(launched=True).order_by('earned_today')[:10]
  return HttpResponse('<h1>This is this</h1>')

def demo_project(request):
  Project.objects.create(
    user_id=1,
    title='demo_title',
    subtitle='demo_subtitle',
    location='demo_location',
    image='demo_image',
    video='demo_video',
    type='demo_type',
    goal=1.56,
    main_category='demo_mc',
    main_subcat='demo_ms',
    second_cat='demo_sc',
    second_subcat='demo_ss',
    launch_date=datetime.now(),
    end_date=datetime.now(),
    launched=True,
  )

  return HttpResponse('<h1>Done!</h1>')
