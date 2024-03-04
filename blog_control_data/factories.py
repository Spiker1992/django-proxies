import factory
from . import models

class PostFactory(factory.django.DjangoModelFactory):
    subject = "Hello World"
    content = "Lorem Ipsum"
    
    class Meta:
        model = models.Post