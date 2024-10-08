from django.apps import AppConfig


class AboutusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.aboutus'
    verbose_name = 'About Us'

    def ready(self) -> None:
        from . import signals
