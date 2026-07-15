from django.contrib import admin
from . models import (
    Biography,
    Journey,
    Experience,
    Education,
    Certification,
    Technology,
    TechnologyCategory,
    FunFact,
    SocialLink
)

# Register your models here.
@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = (
        'heading',
        'years_of_experience',
        'projects_completed',
        'updated_at',
    )
    
    search_fields = (
        'heading',
        'subtitle',
    )
    
@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = (
        'year',
        'title',
        'order',
    )
    
    ordering = ('order',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'company',
        'currently_working',
        'start_date',
        'end_date',
    )
    
    list_filter = (
        'currently_working',
    )
    
    ordering = ('order',)
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'institution',
        'degree',
        'start_year',
        'end_year',
    )
    
    ordering = ('order',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'issuer',
        'issue_date',
    )
    
    search_fields = (
        'title',
        'issuer',
    )
    
@admin.register(TechnologyCategory)
class TechnologyCategoryAdmin(admin.ModelAdmin):
    list_display =('name',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'proficiency',
        'years',
    )
    
    list_filter = (
        'category',
    )
    
    ordering = (
        'category',
        'order',
    )
    
@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
    )
    
    ordering = ('order',)
    
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        'platform',
        'url',
    )
    
    ordering = ('order',)

    