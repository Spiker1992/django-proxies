from dataclasses import dataclass
from typing import Any, Optional
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.db import models
from pydantic import BaseModel


@dataclass
class Empty:
    ...

@dataclass
class PostCreated:
    title: str

@dataclass
class PostUpdated:
    content: str
    title: str

class PostEvents(models.Model):
    event_type = models.CharField(max_length=50)
    event_payload = models.JSONField()
    EVENT_TYPE = None
    PAYLOAD_DATACLASS = Empty

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "event_payload":
            if __value:
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
    EVENT_TYPE = "review_for_review"
    PAYLOAD_DATACLASS = Empty
    
    class Meta:
        proxy = True 

