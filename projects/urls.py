from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.demo_project, name='projects')
]
