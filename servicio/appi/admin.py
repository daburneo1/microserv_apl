from django.contrib import admin
from .models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

admin.site.register(AuthUser, AuthorAdmin)
