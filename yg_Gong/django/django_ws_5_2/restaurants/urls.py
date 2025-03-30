from django.urls import path
from . import views


app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 단건조회(상세조회)
    path('<int:restaurant_pk>/',views.detail, name='detail'),
    # 수정 페이지
    path('<int:restaurant_pk>/edit',views.edit, name='edit'),
    # DB 수정
    path('<int:restaurant_pk>/update',views.update, name='update'),
    # DB 삭제
    path('<int:restaurant_pk>/delete',views.delete, name='delete'),
]