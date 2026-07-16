from django.db import models

# Create your models here.
class Biography(models.Model):
    heading = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)

    biography = models.TextField()

    profile_image = models.ImageField(
        upload_to="about/profile/"
    )

    resume = models.FileField(
        upload_to="about/resume/",
        blank=True,
        null=True
    )

    years_of_experience = models.PositiveIntegerField(default=0)

    projects_completed = models.PositiveIntegerField(default=0)

    github_url = models.URLField(blank=True)

    linkedin_url = models.URLField(blank=True)

    email = models.EmailField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Biography"

    def __str__(self):
        return self.heading
    
class BiographyImage(models.Model):
    biography = models.ForeignKey(
        Biography,
        on_delete=models.CASCADE,
        related_name="images"
    )
    
    image = models.ImageField(
        upload_to="about/biography/"
    )
    alt_text = models.ImageField(
        max_length=100,
        blank=True
    )
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"image {self.order}"

class Journey(models.Model):
    year = models.CharField(max_length=20)

    title = models.CharField(max_length=100)

    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
class Experience(models.Model):

    company = models.CharField(max_length=120)

    position = models.CharField(max_length=120)

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(default=False)

    description = models.TextField()

    technologies = models.CharField(
        max_length=250,
        help_text="Separate with commas."
    )

    company_logo = models.ImageField(
        upload_to="experience/",
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.position} - {self.company}"
    
class Education(models.Model):

    institution = models.CharField(max_length=150)

    degree = models.CharField(max_length=150)

    field = models.CharField(max_length=150)

    start_year = models.PositiveIntegerField()

    end_year = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.institution
    
    
class Certification(models.Model):

    title = models.CharField(max_length=150)

    issuer = models.CharField(max_length=150)

    issue_date = models.DateField()

    credential_url = models.URLField(blank=True)

    logo = models.ImageField(
        upload_to="certifications/",
        blank=True
    )

    def __str__(self):
        return self.title
    
class TechnologyCategory(models.Model):
    
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
class TechnologyCategory(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
    proficiency = models.PositiveIntegerField()

    years = models.PositiveIntegerField(default=1)
    
    order = models.PositiveIntegerField(default=0)
    
    
class Technology(models.Model):

    category = models.ForeignKey(
        TechnologyCategory,
        on_delete=models.CASCADE,
        related_name="technologies"
    )

    name = models.CharField(max_length=80)

    icon = models.CharField(
        max_length=100,
        help_text="Font Awesome class."
    )

    proficiency = models.PositiveIntegerField()

    years = models.PositiveIntegerField(default=1)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return self.name
    
    
class FunFact(models.Model):

    icon = models.CharField(max_length=80)

    title = models.CharField(max_length=120)

    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    

class SocialLink(models.Model):

    PLATFORM_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("twitter", "Twitter"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "YouTube"),
    ]

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    icon = models.CharField(max_length=100)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.get_platform_display()
    