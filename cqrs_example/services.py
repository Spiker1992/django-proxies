
from cqrs_example.models import Post
from cqrs_example.models.post import Post

def createBlogPost(subject: str, content: str) -> Post:
    post = Post(subject=subject, content=content)
    post.save()
    
    return post

def retrieveBlogPost(post_id: int) -> Post:
    return Post.objects.get(id=post_id)