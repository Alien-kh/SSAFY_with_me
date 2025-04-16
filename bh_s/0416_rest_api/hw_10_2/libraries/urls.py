from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.booklist),
    path('libraries/<int:pk>/', views.bookdetail),
]
