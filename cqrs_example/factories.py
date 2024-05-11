import factory
from cqrs_example.models.post import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post