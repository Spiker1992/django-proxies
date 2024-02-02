from blog.models.post import Post


class PublishedPost(Post):

    class Meta:
        proxy = True

    def performance(self):
      ...