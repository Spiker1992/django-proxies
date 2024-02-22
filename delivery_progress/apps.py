from django.apps import AppConfig

class DeliveryProgressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery_progress'

    def ready(self):
        from . import signals, listeners

        signals.order_was_paid.connect(listeners.mark_order_as_paid)
        signals.order_was_picked_up.connect(listeners.mark_order_as_picked_up)
