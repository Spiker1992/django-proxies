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

    @property
    def __status_changed(self) -> bool:
        current_status = Mapper.resolve_proxy_status(self.__class__)
        return  current_status != self.status 

    def clean(self):
        if self.__status_changed and self.status not in self.ALLOWED_TRANSITIONS:
            raise ValueError(f"Invalid status: {self.status}. Valid statuses are: {[values for values in self.ALLOWED_TRANSITIONS]}")
        
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)

        if self.__status_changed:
            self._resolve_proxy_model()