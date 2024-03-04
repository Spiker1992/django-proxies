
from blog_control_data.constants import STATUS_DRAFT, STATUS_PUBLISHED
from blog_control_data.models.post import Post


class ReadyForReviewPost(Post):
    ALLOWED_TRANSITIONS = [
        STATUS_DRAFT,
        STATUS_PUBLISHED,
    ]

    class Meta:
        proxy = True
