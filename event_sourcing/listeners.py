from django.db.models.signals import post_save
from django.dispatch import receiver

from event_sourcing.models.events import CreatedPostEvent
from event_sourcing.models.projections import Post


@receiver(post_save, sender=CreatedPostEvent)
def projection(sender, instance, **kwargs): 
    post = Post()
    post.writable()

    post.stream_id = instance.stream_id
    post.title = instance.event_payload.get("title")
    post.save()

@receiver(post_save, sender=CreatedPostEvent)
def reactor(sender, instance, **kwargs): 
    print(f"send email: {instance.stream_id} {instance.event_payload.get('title')}")