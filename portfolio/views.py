from django.shortcuts import render
from datetime import date

from skills.models import Skill
from projects.models import Project
from blog.models import BlogPost


def home(request):

    featured_skills = (
        Skill.objects
        .filter(featured=True)[:6]
    )

    featured_projects = (
        Project.objects
        .filter(featured=True)
        .prefetch_related("technologies")[:4]
    )

    latest_posts = (
        BlogPost.objects
        .filter(status="published")
        .order_by("-published_at")[:3]
    )

    context = {
        "featured_skills": featured_skills,
        "featured_projects": featured_projects,
        "latest_posts": latest_posts,
        "current_year": date.today().year,
    }

    return render(request, "home/home.html", context)