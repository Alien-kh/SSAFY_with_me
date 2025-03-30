from django.shortcuts import render, redirect
from .models import Restaurant

app_name = 'restaurants'

# Create your views here.
def index(request): 
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(reqeust):
    restaurant = Restaurant()
    restaurant.name = reqeust.POST.get('name')
    restaurant.description = reqeust.POST.get('description')
    restaurant.address = reqeust.POST.get('address')
    restaurant.phone_number = reqeust.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')

#단건조회
def detail(request,restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant': restaurant
    }
    return render(request,'restaurants/detail.html', context)

# 수정 페이지
def edit(request,restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant': restaurant
    }

    return render(request, 'restaurants/edit.html', context)

# DB 수정
def update(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()

    return redirect('restaurants:detail', restaurant.pk )

# DB 삭제
def delete(reques,restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.delete()
    return redirect('restaurants:index')