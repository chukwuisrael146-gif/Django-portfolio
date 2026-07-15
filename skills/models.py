from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="skills/")
    percentage = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-percentage"]

    def __str__(self):
        return self.title

    @property
    def level(self):
        if self.percentage >= 90:
            return "Advanced"
        elif self.percentage >= 75:
            return "Intermediate"
        return "Learning"