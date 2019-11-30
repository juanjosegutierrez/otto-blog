from django.db import models

class Article():
    title = models.TextField()
    subtitle = models.TextField()
    author = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
