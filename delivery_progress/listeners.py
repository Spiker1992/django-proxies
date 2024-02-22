from django.dispatch import receiver

from delivery_progress.models import STATUS_ORDER_PAID, STATUS_ORDER_PICKED_UP, Delivery


def mark_order_as_paid(sender, order_id, **kwargs):
    delivery: Delivery = (
        Delivery.objects
            .filter(order_id=order_id)
            .get()
    )

    delivery.status = STATUS_ORDER_PAID
    delivery.save()

def mark_order_as_picked_up(sender, order_id, **kwargs):
    delivery: Delivery = (
        Delivery.objects
            .filter(order_id=order_id)
            .get()
    )

    delivery.status = STATUS_ORDER_PICKED_UP
    delivery.save()