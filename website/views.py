from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("website:home")
        else:
            messages.success(
                request, "There was an error logging in. Please try again."
            )
            return redirect("website:home")

    return render(request, "website/home.html", {})


def logout_user(request):
    pass
