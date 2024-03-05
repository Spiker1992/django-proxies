from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.db import models
from pydantic import BaseModel

class CreatePost(BaseModel):
    title: str


class PostEvents(models.Model):
    event_type = models.CharField(max_length=50)
    event_payload = models.JSONField()

    def save(self, *args, **kwargs):
        self.clean()

        super().save(*args, **kwargs)

class CreatedPostEvent(PostEvents):
    event_type = "created_post"

    def clean(self):
        try:
            CreatePost(**self.event_payload)
        except ValidationError as e:
            raise ValueError(f"Invalid payload structure: {e}")
        except TypeError as e:
            raise ValueError(f"Invalid payload type")

    class Meta:
        proxy = True 

