from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)

    WRITABLE = False

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
    