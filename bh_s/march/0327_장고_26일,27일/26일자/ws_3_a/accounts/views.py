from django.shortcuts import render

# Create your views here.
def loginview(request):

    id = request.GET.get('id')
    password = request.GET.get('password')

    context = {
        'id': id,
        'password': password
    }
    return render(request, 'accounts/accounts.html', context)