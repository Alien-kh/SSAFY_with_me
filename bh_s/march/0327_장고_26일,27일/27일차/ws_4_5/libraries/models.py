from django.db import models
import requests

class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_URL = "https://www.aladin.co.kr/ttb/api/ItemList.aspx"
        params = {
            "ttbkey": "",  # 알라딘 API 키 입력
            "QueryType": "ItemNewAll",
            "MaxResults": 10,
            "start": 1,
            "SearchTarget": "Book",
            "output": "js",
            "Version": "20131101"
        }
        
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        if "item" in data:
            for item in data["item"]:
                book, created = cls.objects.get_or_create(
                    isbn=item.get("isbn"),
                    defaults={
                        "title": item.get("title"),
                        "author": item.get("author", ""),
                        "category_name": item.get("categoryName", ""),
                        "category_id": item.get("categoryId", 0),
                        "pub_date": item.get("pubDate"),
                        "price": item.get("priceStandard", 0),
                        "fixed_price": item.get("fixedPrice", False)
                    }
                )
                
                if created:
                    print(f"Book '{book.title}' inserted.")
                else:
                    print(f"Book '{book.title}' already exists.")