
from blog_state_pattern.constants import STATUS_DRAFT, STATUS_PUBLISHED
from blog_state_pattern.models.post import Post


class ReadyForReviewPost(Post):
    ALLOWED_TRANSITIONS = [
        STATUS_DRAFT,
        STATUS_PUBLISHED,
    ]

    class Meta:
        proxy = True
