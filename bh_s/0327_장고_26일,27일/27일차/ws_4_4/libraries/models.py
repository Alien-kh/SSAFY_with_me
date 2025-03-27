from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)  # isbn 
    title = models.TextField()      # 책 제목
    pub_date = models.DateField()   # 출간일(출시일)
    author = models.TextField()     # 저자
    category_name = models.TextField()  # 분야명
    category_id = models.IntegerField() # 분야 id
    price = models.IntegerField()       # 가격
    fixed_price = models.BooleanField() # 고정 가격 여부
    adult = models.BooleanField()       # 성인 등급 여부
    