from blog_control_data.constants import STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_control_data.models.post_proxies.draft_post import DraftPost
from blog_control_data.models.post_proxies.ready_for_review_post import ReadyForReviewPost
import pytest
from django.test import TestCase
from blog_control_data.factories import PostFactory
from blog_control_data.models.post import Post

@pytest.mark.django_db
class TestTransitions(TestCase):
    def test_invalid_transition(self):
        post: Post = PostFactory.create()
        post.status = STATUS_PUBLISHED

        expeced_error_message = "ValueError: Invalid status: published. Valid statuses are: ['ready_for_review']"

        with self.assertRaises(ValueError, msg=expeced_error_message):
            post.save()

    def test_dont_change_transition(self):
        post: Post = PostFactory.create()
        post.save()


        assert  isinstance(post, DraftPost)

    def test_successful_transition(self):
        post: Post = PostFactory.create()
        post.status = STATUS_READY_FOR_REVIEW
        post.save()

        assert  isinstance(post, ReadyForReviewPost)

    def test_disable_status_change_when_no_transitions_exist(self):
        post: Post = PostFactory.create(status=STATUS_PUBLISHED)
        post.status = STATUS_READY_FOR_REVIEW

        expeced_error_message = "ValueError: Invalid status: published. Valid statuses are: []"

        with self.assertRaises(ValueError, msg=expeced_error_message):
            post.save()