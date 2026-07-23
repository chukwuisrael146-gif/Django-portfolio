from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Technology,
    Project,
    ProjectImage,
    ProjectFeature,
    DevelopmentStage,
)


# =====================================================
# TECHNOLOGY
# =====================================================

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "icon_preview",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

    def icon_preview(self, obj):
        return format_html(
            '<i class="{}" style="font-size:20px;color:#f97316;"></i>',
            obj.icon
        )

    icon_preview.short_description = "Icon"


# =====================================================
# INLINES
# =====================================================

class ProjectImageInline(admin.TabularInline):

    model = ProjectImage
    extra = 1
    ordering = ("order",)


class ProjectFeatureInline(admin.TabularInline):

    model = ProjectFeature
    extra = 1
    ordering = ("order",)


class DevelopmentStageInline(admin.TabularInline):

    model = DevelopmentStage
    extra = 1
    ordering = ("order",)


# =====================================================
# PROJECT
# =====================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    save_on_top = True

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_display = (
        "thumbnail_preview",
        "title",
        "category",
        "colored_status",
        "client",
        "featured",
        "completed_date",
    )

    list_filter = (
        "featured",
        "status",
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
        "role",
        "short_description",
        "description",
        "challenge",
        "solution",
    )

    ordering = (
        "-featured",
        "order",
        "-completed_date",
    )

    list_per_page = 15

    date_hierarchy = "completed_date"

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
                "status",
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

        ("Project Content", {

            "fields": (

                "short_description",
                "description",

            )

        }),

        ("Case Study", {

            "classes": ("wide",),

            "fields": (

                "challenge",
                "solution",
                "outcome",
                "lessons_learned",

            )

        }),

        ("Project Information", {

            "fields": (

                "client",
                "role",
                "team_size",
                "duration",
                "completed_date",
                "version",
                "order",

            )

        }),

        ("Project Statistics", {

            "classes": ("collapse",),

            "fields": (

                "lines_of_code",
                "commits",

            )

        }),

        ("Technology Stack", {

            "fields": (

                "technologies",

            )

        }),

        ("Links", {

            "classes": ("collapse",),

            "fields": (

                "github_url",
                "live_url",

            )

        }),

        ("SEO", {

            "classes": ("collapse",),

            "fields": (

                "meta_description",

            )

        }),

    )

    inlines = [

        ProjectImageInline,

        ProjectFeatureInline,

        DevelopmentStageInline,

    ]

    def thumbnail_preview(self, obj):

        if obj.thumbnail:

            return format_html(

                '<img src="{}" width="70" height="50" style="object-fit:cover;border-radius:10px;">',

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
                    padding:15px;
                    border-radius:18px;
                    background:#111827;
                ">

                    <img
                        src="{}"
                        width="420"
                        style="
                            border-radius:14px;
                            display:block;
                            object-fit:cover;
                        ">

                </div>
                """,
                obj.thumbnail.url,
            )

        return "No thumbnail uploaded."

    thumbnail_preview_large.short_description = "Thumbnail Preview"

    def colored_status(self, obj):

        colors = {

            "Planning": "#3b82f6",

            "In Progress": "#f59e0b",

            "Completed": "#10b981",

            "Archived": "#6b7280",

        }

        color = colors.get(obj.status, "#6b7280")

        return format_html(
            """
            <span style="
                background:{};
                color:white;
                padding:5px 12px;
                border-radius:999px;
                font-size:12px;
                font-weight:600;">
                {}
            </span>
            """,
            color,
            obj.status,
        )

    colored_status.short_description = "Status"