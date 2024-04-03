from django.apps import AppConfig


class EventSourcingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_sourcing'

    def ready(self):
        from . import listeners