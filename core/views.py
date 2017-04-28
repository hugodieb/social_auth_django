from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')
