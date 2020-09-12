from django.apps import AppConfig


class MagzineConfig(AppConfig):
    name = 'myproject.apps.magzine'
    verbose_name = _("Magzine")

    def ready(self):
        from . import signals
