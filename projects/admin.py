from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Technology,
    Project,
    ProjectImage,
    ProjectFeature,
)


# ===========================
# Technology
# ===========================

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "icon_preview",
    )

    search_fields = (
        "name",
    )

    def icon_preview(self, obj):
        return format_html(
            '<i class="{}" style="font-size:22px;color:#f97316;"></i>',
            obj.icon
        )

    icon_preview.short_description = "Icon"


# ===========================
# Gallery Inline
# ===========================

class ProjectImageInline(admin.TabularInline):

    model = ProjectImage

    extra = 1

    fields = (
        "image",
        "caption",
        "order",
    )


# ===========================
# Features Inline
# ===========================

class ProjectFeatureInline(admin.TabularInline):

    model = ProjectFeature

    extra = 1

    fields = (
        "icon",
        "title",
        "description",
    )


# ===========================
# Project
# ===========================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_display = (
        "thumbnail_preview",
        "title",
        "category",
        "client",
        "featured",
        "completed_date",
    )

    list_filter = (
        "featured",
        "category",
        "completed_date",
    )

    search_fields = (
        "title",
        "client",
        "short_description",
    )

    ordering = (
        "order",
        "-completed_date",
    )

    filter_horizontal = (
        "technologies",
    )

    readonly_fields = (
        "thumbnail_preview_large",
    )

    fieldsets = (

        ("Basic Information", {

            "fields": (

                "title",
                "slug",
                "category",
                "featured",

            )

        }),

        ("Images", {

            "fields": (

                "thumbnail",
                "thumbnail_preview_large",
                "hero_image",

            )

        }),

        ("Content", {

            "fields": (

                "short_description",
                "description",

            )

        }),

        ("Project Details", {

            "fields": (

                "client",
                "duration",
                "completed_date",
                "order",

            )

        }),

        ("Links", {

            "fields": (

                "github_url",
                "live_url",

            )

        }),

        ("Technology Stack", {

            "fields": (

                "technologies",

            )

        }),

    )

    inlines = [

        ProjectImageInline,

        ProjectFeatureInline,

    ]

    def thumbnail_preview(self, obj):

        if obj.thumbnail:

            return format_html(

                '<img src="{}" width="70" style="border-radius:10px;">',

                obj.thumbnail.url

            )

        return "-"

    thumbnail_preview.short_description = "Preview"

    def thumbnail_preview_large(self, obj):

        if obj.thumbnail:

            return format_html(

                '<img src="{}" width="350" style="border-radius:18px;">',

                obj.thumbnail.url

            )

        return "No Image"

    thumbnail_preview_large.short_description = "Thumbnail Preview"