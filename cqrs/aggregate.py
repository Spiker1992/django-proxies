from dataclasses import asdict
from cqrs.models import CreatedPostEvent
from cqrs.models.post_events import PostCreated, PostEvents, PostUpdatedEvent, ReadyForReviewEvent


class PostAggregate():
    events = []
    mapper  = {
       CreatedPostEvent: "apply_created_post_event",
       PostUpdatedEvent: "apply_updated_post_event",
       ReadyForReviewEvent: "apply_ready_for_review_event",
    }
    title = None 
    content = None 
    ready_for_review = False

    def __init__(self) -> None:
        self.events = []

    def load(self, stream_id):
        events = list(PostEvents.objects.filter(stream_id=stream_id).all())

        for event in events:
            self.__apply_event(event)

    def __apply_event(self, event):
        apply_method_name = self.mapper.get(event.__class__)
        
        self.__getattribute__(apply_method_name)(event)

    def __persist_event(self, event):
        event.save()

    def create_post(self, stream_id: int, payload: PostCreated):
        event = CreatedPostEvent(stream_id=stream_id, event_payload=asdict(payload))

        self.__apply_event(event)
        self.__persist_event(event)


    def apply_created_post_event(self, event):
        self.title = event.event_payload.get("title")
        self.events.append(event)

    def apply_updated_post_event(self, event):
        self.title = event.event_payload.get("title")
        self.content = event.event_payload.get("content")
        self.events.append(event)

    def apply_ready_for_review_event(self, event):
        self.ready_for_review = True
        self.events.append(event)