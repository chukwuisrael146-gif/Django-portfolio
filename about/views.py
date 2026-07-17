from django.shortcuts import render
from .models import Biography, Journey, Experience, TechStack

# Create your views here.
def about(request):

    biography = Biography.objects.first()
    journey = Journey.objects.all()
    experiences = Experience.objects.all()
    tech_stack = TechStack.objects.all()

    context = {
        'biography': biography,
        'journey': journey,
        'experiences': experiences,
        'tech_stack': tech_stack,
    }
    return render(request, "about/about.html", context)

