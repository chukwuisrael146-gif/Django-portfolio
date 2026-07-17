from django.shortcuts import render
from .models import Biography, Journey, Experience

# Create your views here.
def about(request):

    biography = Biography.objects.first()
    journey = Journey.objects.all()
    experiences = Experience.objects.all()

    context = {
        'biography': biography,
        'journey': journey,
        'experiences': experiences,
    }
    return render(request, "about/about.html", context)

