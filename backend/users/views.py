from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
  return HttpResponse('<h1>I hate this</h1>')

def demo_user(request):
  user = User.objects.create_user(
    username='demo',
    password='password',
    email='demouser@aa.io',
    first_name='Demo',
    last_name='User'
  )

  return HttpResponse(f'<h1>{user.to_dict()}</h1>')
