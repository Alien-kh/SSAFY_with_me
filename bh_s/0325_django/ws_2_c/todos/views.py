from django.shortcuts import render


# Create your views here.
# 메인 페이지 (할 일 목록)
def index(request):
    work = request.GET.get('work')  # GET 요청에서 'work' 값 받기
    return render(request, 'todos/index.html', {'work': work})

# 할 일 생성 페이지
def create_todo(request):
    return render(request, 'todos/create_todo.html')

# 상세 페이지 (variable routing 사용)
def detail(request, work):
    return render(request, 'todos/detail.html', {'work': work})