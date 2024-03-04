from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)

    def writable(self):
        ...

    def save(self):
        raise Exception("This model is ready only")
    
    def delete(self):
        raise Exception("This model is ready only")
