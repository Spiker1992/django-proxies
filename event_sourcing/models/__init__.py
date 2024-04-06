
from ..state import Mapper
from .event_streams import *
from .events import *
from .projections import *

Mapper.state = {
    "created_post": CreatedPostEvent,
    "post_updated": PostUpdatedEvent,
    "ready_for_review": ReadyForReviewEvent,
}
