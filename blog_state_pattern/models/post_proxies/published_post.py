from blog_state_pattern.models.post import Post


class PublishedPost(Post):

    class Meta:
        proxy = True

    def performance(self):
      ...