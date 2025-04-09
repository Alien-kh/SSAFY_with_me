from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:restaurant_pk>/', views.detail, name='detail'),
    path('<int:restaurant_pk>/menus/create/', views.menus_create, name='menus_create'),
    path('<int:restaurant_pk>/menus/<int:menu_pk>/update/', views.menus_update, name='menus_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
