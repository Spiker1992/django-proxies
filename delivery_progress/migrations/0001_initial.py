# Generated by Django 5.0.1 on 2024-02-22 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('order_received', 'Order Received'), ('order_paid', 'Order Paid'), ('order_picked_up', 'Order Picked Up'), ('order_awaiting_shipment', 'Order Awaiting Shipment'), ('order_shipped', 'Order Shipped'), ('order_at_delivery_depot', 'Order At Delivery Depot'), ('order_on_its_way', 'Order On Its Way'), ('order_will_be_delivered_soon', 'Order Will Be Delivered Soon'), ('order_was_delivered', 'Order Was Delivered')], default='order_received', max_length=30)),
                ('order_id', models.IntegerField()),
            ],
        ),
    ]
