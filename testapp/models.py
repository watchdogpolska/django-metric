from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
