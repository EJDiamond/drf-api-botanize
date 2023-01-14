from django.db import models
from django.contrib.auth.models import User
from answers.models import Answer


class Like(models.Model):
    """
    Model to enable user to like other users answers
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        """
        ensures the user can't like the same answer twice
        """
        unique_together = ['owner', 'answer']

        def __str__(self):
            return f'{self.owner} {self.answer}'
