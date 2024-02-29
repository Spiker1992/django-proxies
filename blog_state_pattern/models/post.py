from abc import abstractmethod
from typing import Any
from django.db import models
from blog_state_pattern.state import Mapper

from blog_state_pattern.constants import STATUS_DRAFT



class Post(models.Model):
    subject = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(max_length=30, default=STATUS_DRAFT)

    ALLOWED_TRANSITIONS = []

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._resolve_proxy_model()

    def _resolve_proxy_model(self):
        proxy_class = Mapper.state.get(self.status)

        if proxy_class:
            self.__class__ = proxy_class

        return self
    
    def transition_to(self, state: str):
        if state not in self.ALLOWED_TRANSITIONS:
            raise ValueError(f"Cannot transition to '{state}'")
        
        self.status = state
        self.save()

        self._resolve_proxy_model()

        return self
