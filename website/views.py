from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login, logout


# Create your views here.
def home(request):
    return render(request, "website/home.html", {})


def login_user(request):
    pass


def logout_user(request):
    pass
