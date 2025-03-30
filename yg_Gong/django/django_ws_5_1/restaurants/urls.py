from django.urls import path
from . import views
app_name = 'restaurants'

urlpatterns = [
    # 전체조회
    path('', views.main, name='main'),

    # 식당 등록 화면
    path('write/', views.write, name='write'),

    # 식당 DB 등록
    path('create/', views.create, name='create'),


]
