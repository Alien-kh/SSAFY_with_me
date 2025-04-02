from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)