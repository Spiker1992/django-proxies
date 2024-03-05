import pytest
from django.test import TestCase
from cqrs.models import CreatedPostEvent, Post

@pytest.mark.django_db
class TestReadModel(TestCase):
    def test_read_model_cannot_be_saved(self):
        post: Post = Post()

        with self.assertRaises(Exception, msg="This model is ready only"):
            post.save()

    def test_read_model_cannot_be_deleted(self):
        post: Post = Post()

        with self.assertRaises(Exception, msg="This model is ready only"):
            post.delete()

@pytest.mark.django_db
class TestWriteModel(TestCase):
    def test_allow_writes_if_writes_are_whitelisted(self):
        post: Post = Post()
        post.writable()

        post.title = "Hello World"
        post.save()

        post.refresh_from_db()
        assert post.title == "Hello World"
    
    def test_allow_deletion_of_the_model(self):
        post: Post = Post()
        post.writable()

        post.title = "Hello World"
        post.save()
        id = post.pk
        post.delete()

        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=id) 


@pytest.mark.django_db
class TestCreateEvent(TestCase):
    def test_create_post_event_with_payload_being_a_text(self):
        post_event = CreatedPostEvent()
        post_event.event_payload =  "TEST"

        with self.assertRaises(ValueError):
            post_event.save()

    def test_create_post_event_with_invalid_payload(self):
        post_event = CreatedPostEvent()
        post_event.event_payload =  { "Hello": "World"}
        
        with self.assertRaises(ValueError):
            post_event.save()


    def test_create_post_event_with_valid_payload(self):
        post_event = CreatedPostEvent()
        post_event.event_payload =  { "title": "Hello World"}
        
        post_event.save()