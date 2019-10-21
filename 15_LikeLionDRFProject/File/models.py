from django.db import models
from django.conf import settings


class File(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    files = models.FileField(
        blank=False,
        null=False,
        upload_to="files"
    )
    desc = models.CharField(max_length=100)
