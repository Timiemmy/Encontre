from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date = models.DateField(auto_now_add=True)
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	likes = models.ManyToManyField(CustomUser, related_name='likes', blank=True)
