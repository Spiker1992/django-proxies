import django.dispatch

order_was_paid = django.dispatch.Signal()
order_was_picked_up = django.dispatch.Signal()
order_awaiting_shipment = django.dispatch.Signal()

