from django.contrib import admin

from .models import UserProfile,User


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user','rol_student','rol_teacher']

admin.site.register(UserProfile, UserProfileAdmin)
