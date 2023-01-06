from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)
