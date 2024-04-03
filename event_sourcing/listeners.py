from django.db.models.signals import post_save
from django.dispatch import receiver

from event_sourcing.models.post_events import CreatedPostEvent
from event_sourcing.models.post import Post


@receiver(post_save, sender=CreatedPostEvent)
def projection(sender, instance, **kwargs): 
    post = Post()
    post.writable()
    print(instance.__dict__)
    post.stream_id = instance.stream_id
    post.title = instance.event_payload.get("title")
    post.save()

@receiver(post_save, sender=CreatedPostEvent)
def reactor(sender, instance, **kwargs): 
    print(f"send email: {instance.stream_id} {instance.event_payload.get('title')}")