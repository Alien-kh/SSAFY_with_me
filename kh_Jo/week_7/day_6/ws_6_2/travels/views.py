from django.shortcuts import render, redirect
from .models import Travels
from .forms import TravelsForm
# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels' : travels,
    }
    return render(request, 'travels/index.html', context)


def detail(request, pk):
    travel = Travels.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = TravelsForm(request.POST)
        if form.is_valid():
            travels = form.save()
            return redirect('travels:detail', travels.pk)
    else:
        form = TravelsForm()
    
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)

def delete(request, pk):
    travels = Travels.objects.get(pk=pk)
    travels.delete()
    return redirect('travels:index')

def update(request, pk):
    travels = Travels.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelsForm(request.POST, instance=travels)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travels.pk)
    else:
        form = TravelsForm(instance=travels)
    context = {
        'travels' : travels,
        'form' : form,
    }
    return render(request, 'travels/update.html', context)