from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
]
