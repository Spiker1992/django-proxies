from django.db import models

from cqrs_example.constants import STATUS_DRAFT

class Post(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(max_length=30, default=STATUS_DRAFT)
    
    # bloated model...
