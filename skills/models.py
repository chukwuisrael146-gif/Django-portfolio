from django.db import models


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("Backend", "Backend"),
        ("Frontend", "Frontend"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Design", "Design"),
    ]

    title = models.CharField(max_length=100)

    icon = models.CharField(max_length=100)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    percentage = models.PositiveIntegerField(default=80)

    years_of_experience = models.PositiveIntegerField(default=1)

    projects = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True)

    featured = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    @property
    def level(self):
        if self.percentage >= 90:
            return "Advanced"
        elif self.percentage >= 75:
            return "Intermediate"
        return "Learning"