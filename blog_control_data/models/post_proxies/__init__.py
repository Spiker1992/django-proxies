from blog_control_data.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_control_data.state import Mapper
from blog_control_data.models.post_proxies.draft_post import DraftPost
from blog_control_data.models.post_proxies.published_post import PublishedPost
from blog_control_data.models.post_proxies.ready_for_review_post import ReadyForReviewPost

Mapper.state = {
    STATUS_DRAFT: DraftPost,
    STATUS_READY_FOR_REVIEW: ReadyForReviewPost,
    STATUS_PUBLISHED: PublishedPost,
}   