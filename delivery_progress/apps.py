from django.apps import AppConfig

class DeliveryProgressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery_progress'

    def ready(self):
        from . import listeners
