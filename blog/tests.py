from blog.constants import STATUS_READY_FOR_REVIEW
from blog.models.post_proxies.draft_post import DraftPost
from blog.models.post_proxies.ready_for_review_post import ReadyForReviewPost
import pytest
from django.test import TestCase
from blog.factories import PostFactory

@pytest.mark.django_db
class TestPostProxyResolutionAndTransitions(TestCase):
    def test_post_automatically_resolves_to_draft_proxy(self):
        post = PostFactory()
        assert isinstance(post, DraftPost)

    def test_draft_post_transitions_to_ready_for_review_proxy(self):
        post = PostFactory()

        ready_for_review_post = post.complete_state()
        assert isinstance(ready_for_review_post, ReadyForReviewPost) 
        assert ready_for_review_post.status == STATUS_READY_FOR_REVIEW

    