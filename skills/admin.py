from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "percentage",
        "featured",  # Explicitly show featured in list
    )
    fields = [  # Ensure all fields are in the form
        "title",
        "icon",
        "percentage",
        "description",
        "category",
        "years_of_experience",
        "projects",
        "featured",  # Explicitly include featured field
        "order"
    ]
    search_fields = ("title",)
    ordering = ("-percentage",)
