from blog_state_pattern.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog_state_pattern.state import Mapper
from blog_state_pattern.models.post_proxies.draft_post import DraftPost
from blog_state_pattern.models.post_proxies.published_post import PublishedPost
from blog_state_pattern.models.post_proxies.ready_for_review_post import ReadyForReviewPost

Mapper.state = {
    STATUS_DRAFT: DraftPost,
    STATUS_READY_FOR_REVIEW: ReadyForReviewPost,
    STATUS_PUBLISHED: PublishedPost,
}   