from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    query = request.GET.get("q", "").strip()

    posts = (
        BlogPost.objects
        .filter(status="published")
    )

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(context__icontains=query)
        )

    posts = posts.order_by("-published_at")

    featured_post = posts.filter(featured=True).first()

    if featured_post:
        posts = posts.exclude(pk=featured_post.pk)

    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "featured_post": featured_post,
        "page_obj": page_obj,
        "query": query,
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        status="published",
    )

    previous_post = (
        BlogPost.objects
        .filter(
            status="published",
            published_at__lt=post.published_at,
        )
        .order_by("-published_at")
        .first()
    )

    next_post = (
        BlogPost.objects
        .filter(
            status="published",
            published_at__gt=post.published_at,
        )
        .order_by("published_at")
        .first()
    )

    related_posts = (
        BlogPost.objects
        .filter(status="published")
        .exclude(pk=post.pk)[:3]
    )

    context = {
        "post": post,
        "previous_post": previous_post,
        "next_post": next_post,
        "related_posts": related_posts,
    }

    return render(request, "blog/blog_detail.html", context)