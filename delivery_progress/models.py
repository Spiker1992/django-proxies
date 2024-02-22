from django.db import models


STATUS_ORDER_RECEIVED = "order_received" # initial status
STATUS_ORDER_PAID = "order_paid" # triggered by 3rd party payments    

# triggered by our internal packing system
STATUS_ORDER_PICKED_UP = "order_picked_up"
STATUS_ORDER_AWAITING_SHIPMENT = "order_awaiting_shipment"

# triggered by 3rd party courier
STATUS_ORDER_SHIPPED = "order_shipped" 
STATUS_ORDER_AT_DELIVERY_DEPOT = "order_at_delivery_depot"
STATUS_ORDER_ON_ITS_WAY = "order_on_its_way"
STATUS_ORDER_WILL_BE_DELIVERED_SOON = "order_will_be_delivered_soon"
STATUS_ORDER_WAS_DELIVERED = "order_was_delivered"

DELIVERY_STATUSES = (
    (STATUS_ORDER_RECEIVED, "Order Received"),
    (STATUS_ORDER_PAID, "Order Paid"),
    (STATUS_ORDER_PICKED_UP, "Order Picked Up"),
    (STATUS_ORDER_AWAITING_SHIPMENT, "Order Awaiting Shipment"),
    (STATUS_ORDER_SHIPPED, "Order Shipped"),
    (STATUS_ORDER_AT_DELIVERY_DEPOT, "Order At Delivery Depot"),
    (STATUS_ORDER_ON_ITS_WAY, "Order On Its Way"),
    (STATUS_ORDER_WILL_BE_DELIVERED_SOON, "Order Will Be Delivered Soon"),
    (STATUS_ORDER_WAS_DELIVERED, "Order Was Delivered"),
) 

class Delivery(models.Model):
    status = models.CharField(max_length=30, choices=DELIVERY_STATUSES, default=STATUS_ORDER_RECEIVED)
    order_id = models.IntegerField()
