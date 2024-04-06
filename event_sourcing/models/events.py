
from event_sourcing.dataclasses import Empty, PostCreated, PostUpdated
from event_sourcing.models.event_streams import PostEvents

class CreatedPostEvent(PostEvents):
    EVENT_TYPE = "created_post"
    PAYLOAD_DATACLASS = PostCreated

    PROJECTIONS = []
    REACTORS = []

    class Meta:
        proxy = True 


class PostUpdatedEvent(PostEvents):
    EVENT_TYPE = "post_updated"
    PAYLOAD_DATACLASS = PostUpdated

    class Meta:
        proxy = True 

    
class ReadyForReviewEvent(PostEvents):
    EVENT_TYPE = "ready_for_review"
    PAYLOAD_DATACLASS = Empty
    
    class Meta:
        proxy = True 

