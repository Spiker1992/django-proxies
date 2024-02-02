from typing import Any
from django.db import models
from blog.state import Mapper

from blog.constants import STATUS_DRAFT

class Post(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(max_length=30, default=STATUS_DRAFT)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.resolve_proxy_model()

    def resolve_proxy_model(self):
        proxy_class = Mapper.state.get(self.status)

        if proxy_class:
            self.__class__ = proxy_class

        return self
