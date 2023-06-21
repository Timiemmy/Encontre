from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import CustomUser


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    publish_date = models.DateField(default=timezone.now)
    slug = models.SlugField(null=True, max_length=255, unique_for_date='publish_date')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)

    published = PublishedManager()

    class Meta:
        # This will order the posts by the publish date
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['-publish_date'])
        ]  # This will order the post in database

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Using canonical url
        return reverse("detail_post", args=[self.publish_date.year, self.publish_date.month, self.publish_date.day, self.slug])
