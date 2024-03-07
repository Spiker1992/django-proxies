from typing import Any
from django.db import models
from cqrs.dataclasses import Empty, PostCreated, PostUpdated

MAPPER = {}

class PostEvents(models.Model):
    event_type = models.CharField(max_length=50)
    event_payload = models.JSONField()
    stream_id = models.IntegerField()
 
    EVENT_TYPE = None
    PAYLOAD_DATACLASS = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.resolve_proxy_model()

    def resolve_proxy_model(self):
        proxy_class = MAPPER.get(self.event_type)

        if proxy_class:
            self.__class__ = proxy_class

        return self

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "event_payload":
            if __value and self.PAYLOAD_DATACLASS:
                self.PAYLOAD_DATACLASS(**__value)
        
        return super().__setattr__(__name, __value)

    def save(self, *args, **kwargs):
        self.event_type = self.EVENT_TYPE

        super().save(*args, **kwargs)


class CreatedPostEvent(PostEvents):
    EVENT_TYPE = "created_post"
    PAYLOAD_DATACLASS = PostCreated

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


MAPPER = {
    "created_post": CreatedPostEvent,
    "post_updated": PostUpdatedEvent,
    "ready_for_review": ReadyForReviewEvent,
}