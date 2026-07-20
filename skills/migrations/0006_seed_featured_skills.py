# Generated migration to seed initial featured skills

from django.db import migrations


def create_initial_skills(apps, schema_editor):
    Skill = apps.get_model('skills', 'Skill')

    skills = [
        {
            "title": "Django Developer",
            "icon": "fas fa-database",
            "category": "Backend",
            "percentage": 95,
            "years_of_experience": 3,
            "projects": 12,
            "featured": True,
            "order": 1,
        },
        {
            "title": "React Developer",
            "icon": "fab fa-react",
            "category": "Frontend",
            "percentage": 85,
            "years_of_experience": 3,
            "projects": 8,
            "featured": True,
            "order": 2,
        },
        {
            "title": "PostgreSQL",
            "icon": "fas fa-database",
            "category": "Database",
            "percentage": 88,
            "years_of_experience": 2,
            "projects": 10,
            "featured": True,
            "order": 3,
        },
        {
            "title": "UI/UX Design",
            "icon": "fab fa-figma",
            "category": "Design",
            "percentage": 75,
            "years_of_experience": 1,
            "projects": 5,
            "featured": True,
            "order": 4,
        },
        {
            "title": "Git",
            "icon": "fab fa-git-alt",
            "category": "Tools",
            "percentage": 90,
            "years_of_experience": 4,
            "projects": 15,
            "featured": True,
            "order": 5,
        },
        {
            "title": "Docker",
            "icon": "fab fa-docker",
            "category": "Tools",
            "percentage": 78,
            "years_of_experience": 2,
            "projects": 4,
            "featured": True,
            "order": 6,
        },
    ]

    Skill.objects.bulk_create([Skill(**skill) for skill in skills])


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_alter_skill_options_remove_skill_image_and_more'),
    ]

    operations = [
        migrations.RunPython(create_initial_skills),
    ]