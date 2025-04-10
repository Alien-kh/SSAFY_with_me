from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form':comment_form,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.diary = diary
        comment.save()
        return redirect('diaries:index')

