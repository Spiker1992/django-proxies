from blog_state_pattern.constants import STATUS_READY_FOR_REVIEW
from blog_state_pattern.models.post import Post


class DraftPost(Post):
    ALLOWED_TRANSITIONS = [STATUS_READY_FOR_REVIEW]

    class Meta:
        proxy = True

