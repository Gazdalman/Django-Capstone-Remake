from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
  return HttpResponse('<h1>I hate this</h1>')

def demo_user(request):
  User.objects.create(
    username='demo',
    password='password'
  )

  return HttpResponse('<h1>Done</h1>')
