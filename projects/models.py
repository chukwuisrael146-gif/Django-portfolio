from django.db import models
from django.utils.text import slugify

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=100,
        help_text="Font Awesome icon name",
        default="fa-solid fa-code",
        blank=True,
    )
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Technologies'

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
    
    title = models.CharField(max_length=100)

    slug = models.SlugField(
        unique=True,
        help_text="Slug for URL",
        max_length=100,
        blank=True,
        null=True,
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
        default='Web App',
    )
    
    short_description = models.CharField(
        max_length=200,
    )
    
    description = models.TextField()

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
    
    order = models.PositiveIntegerField(default=0)

    completed_date = models.DateField()
    
    duration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="In months",
    )
    
    client = models.CharField(
        max_length=100,
        blank=True,
        default="Personal Project"
    )
    
    featured = models.BooleanField(
        default=False,
        help_text="Display this project on the homepage."
    )
    
    class Meta:
        ordering = ['order', "-completed_date"]

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
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    caption = models.CharField(
        max_length=100,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} Image"
    
class ProjectFeature(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features"
    )

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-check"
    )

    title = models.CharField(max_length=100)

    description = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title