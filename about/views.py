from django.shortcuts import render
from .models import Biography, Journey

# Create your views here.
def about(request):
    
    biography = Biography.objects.first()
    journey = Journey.objects.all()

    context = {
        'biography': biography,
        'journey': journey,
    }
    return render(request, "about/about.html", context)

