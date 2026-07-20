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

class ProjectImageInline(admin.StackedInline):

    model = ProjectImage

    extra = 1

    ordering = ("order",)

    classes = ("collapse",)

    fields = (
        "image",
        "image_preview",
        "caption",
        "order",
    )

    readonly_fields = (
        "image_preview",
    )

    def image_preview(self, obj):

        if obj.pk and obj.image:

            return format_html(
                '<img src="{}" width="300" style="border-radius:16px;border:1px solid #ddd;">',
                obj.image.url
            )

        return "Upload an image first."

    image_preview.short_description = "Preview"


# ===========================
# Features Inline
# ===========================

class ProjectFeatureInline(admin.StackedInline):

    model = ProjectFeature

    extra = 1

    classes = ("collapse",)

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
        "technologies",
        "completed_date",
    )
    
    list_editable = (
        "featured",
    )

    search_fields = (
        "title",
        "client",
        "short_description",
        "description",
    )

    ordering = (
        "-featured",
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
            "classes": ("collapse",),
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
                """
                <div style="
                    display:inline-block;
                    padding:12px;
                    border-radius:18px;
                    background:#111827;
                ">
                    <img
                        src="{}"
                        width="420"
                        style="
                            border-radius:14px;
                            display:block;
                        ">
                </div>
                """,
                obj.thumbnail.url,
            )

        return "No thumbnail uploaded."