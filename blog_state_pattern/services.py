

from blog_state_pattern.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_state_pattern.models.fake_user import FakeUser
from blog_state_pattern.models.post import Post



class SubmitPostForReview:
    def __init__(self, post: Post, user: FakeUser):
        if user.type != "author":
            raise ValueError("Only authors can submit posts for review")
        
        # do some checks?

        post.transition_to(STATUS_READY_FOR_REVIEW)

        # perform side effects?


class DeclineSubmittedPost:
    def __init__(self, post: Post, user: FakeUser):
        if user.type != "reviewer":
            raise ValueError("Only reviewers can decline posts")
        
        # do some checks?

        post.transition_to(STATUS_DRAFT)

        # perform side effects?


class AcceptSubmittedPost:
    def __init__(self, post: Post, user: FakeUser):
        if user.type != "reviewer":
            raise ValueError("Only reviewers can accept posts")
        
        # do some checks?

        post.transition_to(STATUS_PUBLISHED)
        
        # perform side effects?