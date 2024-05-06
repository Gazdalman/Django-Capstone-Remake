from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
  projects = Project.objects.filter(launched=True)
