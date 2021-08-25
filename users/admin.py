"""User admin classes."""

#Djando
from django.contrib import admin

#Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin):
    """Profile admin"""
    pass
    #list_display = ('user')

