from dataclasses import asdict
import uuid
from event_sourcing.dataclasses import PostCreated
from event_sourcing.models import CreatedPostEvent
from django.db import models
from event_sourcing.models.post_events import PostEvents, PostUpdatedEvent, ReadyForReviewEvent

class Aggregate():
    events = []
    event_store: models.Model
    mapper  = {}

    def __init__(self) -> None:
        self.events = []

    def _apply_event(self, event):
        apply_method_name = self.mapper.get(event.__class__)
        if apply_method_name:
            self.__getattribute__(apply_method_name)(event)

    def _persist_event(self, event):
        event.save()

    def load(self, stream_id: uuid.UUID):
        events = list(self.event_store.objects.filter(stream_id=stream_id).all())

        for event in events:
            self._apply_event(event)

class PostAggregate(Aggregate):
    # created a mapper for replies
    mapper  = {
       CreatedPostEvent: "_apply_created_post_event",
       PostUpdatedEvent: "_apply_updated_post_event",
       ReadyForReviewEvent: "_apply_ready_for_review_event",
    }
    event_store = PostEvents

    title = None 
    content = None 
    ready_for_review = False

    def create_post(self, payload: PostCreated) -> uuid.UUID: 
        stream_id: uuid.UUID  = uuid.uuid4()
    
        event = CreatedPostEvent(stream_id=stream_id, event_payload=asdict(payload))

        self._apply_event(event)
        self._persist_event(event)

        return stream_id

    def _apply_created_post_event(self, event):
        self.title = event.event_payload.get("title")
        self.events.append(event)

    def _apply_updated_post_event(self, event):
        self.title = event.event_payload.get("title")
        self.content = event.event_payload.get("content")
        self.events.append(event)

    def _apply_ready_for_review_event(self, event):
        self.ready_for_review = True
        self.events.append(event)