from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Project)
admin.site.register(Story)
admin.site.register(Like)


# Unregister the provided model admin:
admin.site.unregister(User)

from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass
