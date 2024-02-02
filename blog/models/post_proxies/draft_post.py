from blog.constants import STATUS_READY_FOR_REVIEW
from blog.models.post import Post


class DraftPost(Post):
    class Meta:
        proxy = True

    def complete_state(self): 
      self.status = STATUS_READY_FOR_REVIEW
      self.save()

      self.resolve_proxy_model()

      return self
