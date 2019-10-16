from django.db import models
from django.conf import settings


class UserPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default=1,
                               on_delete=models.CASCADE)
