from blog_state_pattern.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_state_pattern.models.fake_user import FakeUser
from blog_state_pattern.models.post_proxies.draft_post import DraftPost
from blog_state_pattern.models.post_proxies.ready_for_review_post import ReadyForReviewPost
import pytest
from django.test import TestCase
from blog_state_pattern.factories import PostFactory
from blog_state_pattern.services import AcceptSubmittedPost, SubmitPostForReview, DeclineSubmittedPost
from blog_state_pattern.models.post import Post

@pytest.mark.django_db
class TestTransitions(TestCase):
    def test_submit_post_for_review(self):
        post: Post = PostFactory.create()
        user = FakeUser(type="author")
        SubmitPostForReview(post, user)

        post.status = STATUS_READY_FOR_REVIEW

    def test_decline_submitted_post(self):
        post: Post = PostFactory.create(status=STATUS_READY_FOR_REVIEW)
        user = FakeUser(type="reviewer")
        DeclineSubmittedPost(post, user)

        post.status = STATUS_DRAFT
        
    def test_accept_submitted_post(self):
        post: Post = PostFactory.create(status=STATUS_READY_FOR_REVIEW)
        user = FakeUser(type="reviewer")
        AcceptSubmittedPost(post, user)

        post.status = STATUS_PUBLISHED
    
    def test_invalid_transition(self):
        post: Post = PostFactory.create()

        with self.assertRaises(ValueError):
            post.transition_to(STATUS_PUBLISHED)

