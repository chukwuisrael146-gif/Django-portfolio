from django.db import models
from django.utils.text import slugify

# Create your models here.
class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    
    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
        
    )
    
    excerpt = models.TextField(
        max_length=100,
        default="Development"
    )
    
    context = models.TextField()
    
    reading_time = models.PositiveBigIntegerField(default=5)

    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title