from django.shortcuts import render, redirect
from .models import Travel
from .forms import TravelForm

# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context ={
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TravelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('travels:index')
    else:
        form = TravelForm()
    
    context ={
        'form' : form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travel.objects.get(pk=pk)
    context={
        'travel' : travel
    }
    return render(request, 'travels/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        travel = Travel.objects.get(pk=pk)
        travel.delete()
        return redirect('travels:index')
    return redirect('travels:detail', pk)