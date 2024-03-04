from blog_control_data.constants import STATUS_READY_FOR_REVIEW
from blog_control_data.models.post import Post


class DraftPost(Post):
    ALLOWED_TRANSITIONS = [STATUS_READY_FOR_REVIEW]

    class Meta:
        proxy = True

