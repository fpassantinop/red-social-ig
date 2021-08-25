"""Posts admin classes."""
#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user', 'title')
    list_editable = ('photo',)

    list_filter = (
                'created',
                'modified'
    )
    
