from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blog_img")
    image_thumbnail = ImageSpecField(
        source="image", processors=[ResizeToFill(60, 60)]
    )
