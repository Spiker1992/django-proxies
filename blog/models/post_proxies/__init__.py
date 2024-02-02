from blog.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_READY_FOR_REVIEW
from blog.state import Mapper
from blog.models.post_proxies.draft_post import DraftPost
from blog.models.post_proxies.published_post import PublishedPost
from blog.models.post_proxies.ready_for_review_post import ReadyForReviewPost

Mapper.state = {
    STATUS_DRAFT: DraftPost,
    STATUS_READY_FOR_REVIEW: ReadyForReviewPost,
    STATUS_PUBLISHED: PublishedPost,
}   