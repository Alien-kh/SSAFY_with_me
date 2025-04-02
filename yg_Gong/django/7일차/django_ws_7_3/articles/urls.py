from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)