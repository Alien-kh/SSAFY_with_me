from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def new_todo(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    todo = Todo(work=work, content=content , is_completed=False)
    todo.save()
    return redirect('todos:detail', todo.pk)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect('todos:index')