from .models import Restaurant, Category, Menu
from django import forms
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'