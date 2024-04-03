import uuid
from django.db import models

class Projection(models.Model):
    WRITABLE = False

    class Meta:
        abstract = True

    def writable(self):
        self.WRITABLE = True 

        return self

    def save(self, *args, **kwargs):
        if self.WRITABLE:
            return super().save(args, kwargs)
        
        raise Exception("This model is ready only")
    
    def delete(self, *args, **kwargs):
        if self.WRITABLE:
            return super().delete(args, kwargs)
        
        raise Exception("This model is ready only")

class Post(Projection):
    title = models.CharField(max_length=100)
    stream_id = models.UUIDField(editable=False, default=uuid.uuid4(), primary_key=True)

    