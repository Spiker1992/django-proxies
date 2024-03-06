import factory

from blog_state_pattern.constants import STATUS_PUBLISHED
from . import models

class DraftPostFactory(factory.django.DjangoModelFactory):
    subject = "Hello World"
    content = "Lorem Ipsum"
    
    class Meta:
        model = models.DraftPost


class PublishedPostFactory(factory.django.DjangoModelFactory):
    subject = "Hello World"
    content = "Lorem Ipsum"
    status=STATUS_PUBLISHED
    
    class Meta:
        model = models.PublishedPost