from django.db import models
from django.conf import settings


class Album(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)
