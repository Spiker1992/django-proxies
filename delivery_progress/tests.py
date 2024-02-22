from unittest.mock import MagicMock
import pytest
from django.test import TestCase
from delivery_progress.factories import DeliveryFactory

from delivery_progress.signals import order_was_paid
from delivery_progress.webhooks import dummy_webhook_from_payment_provider, event_received_from_internal_packing_system

@pytest.mark.django_db
class DeliveryTest(TestCase):
    def setUp(self):
        self.sender = MagicMock()  

    def test_order_was_paid_signal(self):
        order_id = 1
        payload = {
            "meta_data": {
                "order_id": order_id
            }
        }
        delivery = DeliveryFactory.create(order_id = order_id)
        
        dummy_webhook_from_payment_provider(payload)

        delivery.refresh_from_db()
        self.assertEqual(delivery.status, "order_paid")

    def test_order_was_picked_up_signal(self):
        order_id = 1
        payload = {
            "type": "order_is_being_processed",
            "order_id": order_id
        }
        delivery = DeliveryFactory.create(order_id = order_id)
        
        event_received_from_internal_packing_system(payload)

        delivery.refresh_from_db()
        self.assertEqual(delivery.status, "order_picked_up")
