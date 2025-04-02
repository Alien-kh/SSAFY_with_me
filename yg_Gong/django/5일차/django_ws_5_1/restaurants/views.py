from django.shortcuts import render, redirect
from .models import Restaurant
# Create your views here.

# 전체조회
def main(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/main.html', context)
# 식당 등록 화면
def write(request):

    return render(request, 'restaurants/write.html')
# 식당 DB 등록
def create(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    
    restaurant = Restaurant(name = name, description = description, address = address, phone_number = phone_number)
    restaurant.save()
    return redirect('/restaurants/')
