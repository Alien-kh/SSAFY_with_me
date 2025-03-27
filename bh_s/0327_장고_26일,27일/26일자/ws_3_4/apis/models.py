from django.db import models

# Create your models here.
class APIINFO(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField()
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    create_at = models.DateTimeField()
    additional_info = models.TextField(default = False)