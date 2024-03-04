import pytest
from django.test import TestCase
from cqrs.models import Post

@pytest.mark.django_db
class TestTransitions(TestCase):
    def test_read_model_cannot_be_saved(self):
        post: Post = Post()

        with self.assertRaises(Exception, msg="This model is ready only"):
            post.save()

    def test_read_model_cannot_be_deleted(self):
        post: Post = Post()

        with self.assertRaises(Exception, msg="This model is ready only"):
            post.delete()