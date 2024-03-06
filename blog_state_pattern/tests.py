from blog_state_pattern.constants import STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_state_pattern.models.post_proxies.draft_post import DraftPost
from blog_state_pattern.models.post_proxies.ready_for_review_post import ReadyForReviewPost
import pytest
from django.test import TestCase
from blog_state_pattern.factories import DraftPostFactory, PublishedPostFactory
from blog_state_pattern.models.post import Post

@pytest.mark.django_db
class TestTransitions(TestCase):
    def test_invalid_transition(self):
        post: Post = DraftPostFactory.create()

        expeced_error_message = "ValueError: Invalid status: published. Valid statuses are: ['ready_for_review']"

        with self.assertRaises(ValueError, msg=expeced_error_message):
            post.status = STATUS_PUBLISHED

        

    def test_dont_change_transition(self):
        post: Post = DraftPostFactory.create()
        post.save()


        assert  isinstance(post, DraftPost)

    def test_successful_transition(self):
        post: Post = DraftPostFactory.create()
        post.status = STATUS_READY_FOR_REVIEW
        post.save()

        assert  isinstance(post, ReadyForReviewPost)

    def test_disable_status_change_when_no_transitions_exist(self):
        post: Post = PublishedPostFactory.create()

        expeced_error_message = "ValueError: Invalid status: published. Valid statuses are: []"

        with self.assertRaises(ValueError, msg=expeced_error_message):
            post.status = STATUS_READY_FOR_REVIEW