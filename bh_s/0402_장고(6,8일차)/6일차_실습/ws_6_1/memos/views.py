from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm

# Create your views here.

def index(request):
    memos = Memo.objects.all()
    context ={
        'memos' : memos
    }
    return render(request, 'memos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MemoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('memos:index')
    else:
        form = MemoForm()
    
    context ={
        'form' : form,
    }
    return render(request, 'memos/create.html', context)


def detail(request, pk):
    memo = Memo.objects.get(pk=pk)
    context ={
        'memo' : memo
    }
    return render(request, 'memos/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        memo = Memo.objects.get(pk=pk)
        memo.delete()
        return redirect('memos:index')
    return redirect('memos:detail', pk)