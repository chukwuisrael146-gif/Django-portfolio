from django.test import SimpleTestCase

from .admin import BlogPostAdmin
from .models import BlogPost


class BlogPostAdminTests(SimpleTestCase):
    def test_admin_configuration_references_existing_model_fields(self):
        model_fields = {field.name for field in BlogPost._meta.get_fields()}

        for field_name in BlogPostAdmin.list_display:
            if isinstance(field_name, str) and not hasattr(BlogPostAdmin, field_name):
                self.assertIn(field_name, model_fields)

        for field_name in BlogPostAdmin.list_filter:
            if isinstance(field_name, str):
                self.assertIn(field_name, model_fields)
