from django.shortcuts import render
from datetime import date

from skills.models import Skill
from projects.models import Project
# from blog.models import Blog


def home(request):

    featured_skills = Skill.objects.filter(featured=True)[:6]
    
    featured_projects = (
        Project.objects
        .filter(featured=True)
        .prefetch_related('technologies')[:4]
    )

    context = {
        "featured_skills": featured_skills,
        "featured_projects": featured_projects,
    }

    return render(request, "home/home.html", context)