from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import Project, Technology


def project_list(request):
    """
    Display all projects.
    """

    projects = (
        Project.objects
        .prefetch_related("technologies")
        .order_by("-featured", "order", "-completed_date")
    )

    featured_projects = projects.filter(featured=True)

    context = {
        "projects": projects,
        "featured_projects": featured_projects,
        "technologies_count": Technology.objects.count(),
    }

    return render(
        request,
        "projects/projects_list.html",
        context,
    )


def project_detail(request, slug):
    """
    Display a single project.
    """

    project = get_object_or_404(
        Project.objects.prefetch_related(
            "technologies",
            "gallery",
            "features",
        ),
        slug=slug,
    )

    related_projects = (
        Project.objects
        .filter(category=project.category)
        .exclude(pk=project.pk)
        .order_by("-featured", "order")[:3]
    )

    context = {
        "project": project,
        "related_projects": related_projects,
    }

    return render(
        request,
        "projects/projects_detail.html",
        context,
    )