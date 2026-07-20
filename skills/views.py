from django.db.models import Avg
from django.shortcuts import render
from django.views.decorators.cache import never_cache

from skills.models import Skill

@never_cache  # Prevent caching issues
def home(request):
    # Force fresh query each time
    featured_skills = Skill.objects.filter(featured=True).order_by("order", "-percentage")[:8]
    all_skills = Skill.objects.all().order_by("order", "-percentage")

    # Calculate average skill level
    avg_percentage = Skill.objects.aggregate(Avg("percentage"))["percentage__avg"] or 0
    average_skill = int(avg_percentage)

    context = {
        "featured_skills": featured_skills,
        "all_skills": all_skills,
        "skills": all_skills,
        "average_skill": average_skill,
    }

    return render(request, "skills/skills.html", context)