from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    verb = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pass


# In the posts app, create a Like model that tracks which users have liked which posts. This model should have a ForeignKey to Post and a ForeignKey to User.
# In a new app called notifications, create a Notification model with fields like recipient (ForeignKey to User), actor (ForeignKey to User), verb (describing the action), target (GenericForeignKey to the object), and timestamp.

