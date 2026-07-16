from django.shortcuts import render
from .models import Biography

# Create your views here.
def about(request):
    
    biography = Biography.objects.first()

    context = {
        'biography': biography
    }
    return render(request, "about/about.html", context)

