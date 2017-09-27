from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        pass
    else:
        pass


def home(request):
    return render(request, 'main/home.html')
