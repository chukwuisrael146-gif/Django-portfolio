from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "featured",
        "published_at",
    )

    list_filter = (
        "status",
        "featured",
    )
    
    search_fields = (
        "title",
        "content",
    )
    
    prepopulated_fields = {
        "slug": ("title",)
    }