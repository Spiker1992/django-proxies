import factory
from . import models

class DeliveryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Delivery