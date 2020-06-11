from django.db import models


class Post(models.Model):
    title   = models.TextField(max_length=150)
    author  = models.TextField(max_length=150, default='Anonymous User')
    content = models.TextField(max_length=1500)
    image   = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __str__(self):
        return self.title