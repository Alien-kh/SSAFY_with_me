from django.db import models

# Create your models here.
class Memo(models.Model):
    summary = models.CharField(max_length=20)   # 한줄 메모
    memo = models.TextField()                   # 메모 상세
    created_at = models.DateTimeField(auto_now_add=True)    # 게시일
    updated_at = models.DateTimeField(auto_now=True)        # 수정일