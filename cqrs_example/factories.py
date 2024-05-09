import factory
from . import models

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post