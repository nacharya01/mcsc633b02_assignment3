import os
import django

def setup_django_environment():
    """Sets up the Django environment for ChatterBot to use ORM properly."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "module.settings")
    django.setup()
