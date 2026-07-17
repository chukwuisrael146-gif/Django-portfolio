from django.shortcuts import render
from .models import Biography, Journey, Experience, TechStack, FunFact

# Create your views here.
def about(request):

    biography = Biography.objects.first()
    journey = Journey.objects.all()
    experiences = Experience.objects.all()
    tech_stack = TechStack.objects.all()
    fun_facts = FunFact.objects.all()

    context = {
        'biography': biography,
        'journey': journey,
        'experiences': experiences,
        'tech_stack': tech_stack,
        'fun_facts': fun_facts,
    }
    return render(request, "about/about.html", context)

