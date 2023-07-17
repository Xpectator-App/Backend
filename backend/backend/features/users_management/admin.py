from django.apps import AppConfig
from django.contrib import admin
from .models import *  

admin.site.register(Login)
admin.site.register(Profile)
admin.site.register(User)

class UserManagementConfig(AppConfig):
    name = 'User management'
    verbose_name = 'User management'
    