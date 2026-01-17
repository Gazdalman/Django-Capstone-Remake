# from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

# Create your views here.
def demo_project(request):
  project = Project.objects.create(
    user_id=User.objects.get(pk=2).id,
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

  return HttpResponse(f'<h1>{project.to_dict()}</h1>')
