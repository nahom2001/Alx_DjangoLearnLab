from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"posted by {self.author}"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


class Like(models.Model):
    pass



# In the posts app, create a Like model that tracks which users have liked which posts. This model should have a ForeignKey to Post and a ForeignKey to User.
# In a new app called notifications, create a Notification model with fields like recipient (ForeignKey to User), actor (ForeignKey to User), verb (describing the action), target (GenericForeignKey to the object), and timestamp.