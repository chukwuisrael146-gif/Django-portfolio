from django.db.models import Avg
from django.shortcuts import render

from .models import Skill


def skills(request):
    skills = Skill.objects.all()

    context = {
        "skills": skills,
        "featured_skills": Skill.objects.filter(featured=True).count(),
        "average_skill": round(
            Skill.objects.aggregate(Avg("percentage"))["percentage__avg"] or 0
        ),
    }

    return render(request, "skills/skills.html", context)