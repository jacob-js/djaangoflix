from django.db import models
from django.utils import timezone

class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        PUBLISH = 'PU', 'Publish',
        DRAFT = 'DR', 'Draft'
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    @property
    def is_published(self):
        return self.active

    def save(self, *args, **kwargs) -> None:
        if self.state == self.VideoStateOptions.PUBLISH and not self.publish_timestamp:
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamp = None
        return super().save(*args, **kwargs)

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "All Video"
        verbose_name_plural = "All Videos"

class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"
