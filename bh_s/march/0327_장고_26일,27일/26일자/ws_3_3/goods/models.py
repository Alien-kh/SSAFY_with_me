from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # 정수와 소수점을 포함해서 10자리 수 표기 : max_digits = 10,  소수점 2자리수까지 표기 : decimal_places = 2
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField()
    # 생성 시간과 수정 시간 정보를 담을 수 있는 필드 생성.
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)