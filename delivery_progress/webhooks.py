from .signals import order_was_paid, order_was_picked_up, order_awaiting_shipment

def dummy_webhook_from_payment_provider(webhook_payload):
    order_id = webhook_payload["meta_data"]["order_id"]

    order_was_paid.send(sender="dummy_webhook_from_payment_provider", order_id=order_id)

def event_received_from_internal_packing_system(event_payload):
    event_type = event_payload["type"]
    order_id = event_payload["order_id"]

    mapper = {
        "order_is_being_processed": order_was_picked_up,
        "order_was_packaged": order_awaiting_shipment,
    }

    signal = mapper.get(event_type)

    if signal:
        signal.send(sender="event_received_from_internal_packing_system", order_id=order_id)