"""User admin classes."""

#Djando
from django.contrib import admin

#Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user', 'phone_number')

