
from blog.constants import STATUS_PUBLISHED
from blog.models.post import Post


class ReadyForReviewPost(Post):

    class Meta:
        proxy = True

    def complete_state(self): 
      self.status = STATUS_PUBLISHED
      self.save()

      self.resolve_proxy_model()

      return self