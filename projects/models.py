from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    name = models.CharField(max_length=100)

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-code",
        blank=True,
        help_text="Font Awesome icon class",
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Project(models.Model):

    CATEGORY_CHOICES = [
        ("Web App", "Web App"),
        ("Portfolio", "Portfolio"),
        ("Management System", "Management System"),
        ("API", "API"),
        ("Desktop App", "Desktop App"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Planning", "Planning"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Archived", "Archived"),
    ]

    title = models.CharField(max_length=100)

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        max_length=100,
    )

    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
    )

    hero_image = models.ImageField(
        upload_to="projects/hero/",
        blank=True,
        null=True,
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Web App",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Completed",
    )

    short_description = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    # ==========================
    # CASE STUDY
    # ==========================

    challenge = models.TextField(
        blank=True,
        help_text="What problem did this project solve?"
    )

    solution = models.TextField(
        blank=True,
        help_text="How was the problem solved?"
    )

    outcome = models.TextField(
        blank=True,
        help_text="What was the final result?"
    )

    lessons_learned = models.TextField(
        blank=True,
        help_text="Lessons learned while building the project."
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
    )

    github_url = models.URLField(
        blank=True,
        null=True,
    )

    live_url = models.URLField(
        blank=True,
        null=True,
    )

    featured = models.BooleanField(
        default=False,
        help_text="Display this project on the homepage.",
    )

    order = models.PositiveIntegerField(default=0)

    completed_date = models.DateField()

    duration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Example: 6 Weeks",
    )

    client = models.CharField(
        max_length=100,
        default="Personal Project",
        blank=True,
    )

    role = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Full Stack Developer",
    )

    team_size = models.PositiveIntegerField(
        default=1,
    )

    version = models.CharField(
        max_length=20,
        blank=True,
        help_text="Example: v1.0",
    )

    lines_of_code = models.PositiveIntegerField(
        default=0,
    )

    commits = models.PositiveIntegerField(
        default=0,
    )

    meta_description = models.CharField(
        max_length=160,
        blank=True,
    )

    class Meta:
        ordering = ["order", "-completed_date"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery",
    )

    image = models.ImageField(
        upload_to="projects/gallery/",
    )

    caption = models.CharField(
        max_length=100,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} Image"


class ProjectFeature(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features",
    )

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-check",
    )

    title = models.CharField(max_length=100)

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class DevelopmentStage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="timeline",
    )

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-code",
    )

    title = models.CharField(max_length=100)

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Development Stage"
        verbose_name_plural = "Development Stages"

    def __str__(self):
        return f"{self.project.title} - {self.title}"