from django.shortcuts import render
from datetime import date

from skills.models import Skill
# from blog.models import Blog


def home(request):

    featured_skills = Skill.objects.filter(featured=True)[:6]

    context = {
        "featured_skills": featured_skills,
    }

    return render(request, "home/home.html", context)