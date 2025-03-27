from django.contrib import admin
from .models import Book
# Register your models here.


admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publisher","pub_date","isbn")
