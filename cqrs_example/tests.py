from cqrs_example.constants import STATUS_DRAFT
from cqrs_example.services import createBlogPost, retrieveBlogPost
import pytest
from django.test import TestCase
from cqrs_example.factories import PostFactory
from cqrs_example.models import Post

@pytest.mark.django_db
class TestCreatePost(TestCase):
    def test_post_can_be_created(self):
        blog_post = createBlogPost("Hello World", "Lorem Ipsum")
        assert blog_post.status == STATUS_DRAFT
        assert blog_post.pk is not None
    
@pytest.mark.django_db
class TestRetrievePost(TestCase):
    def test_post_can_be_created(self):
        blog_post = PostFactory()

        assert blog_post == retrieveBlogPost(blog_post.pk)