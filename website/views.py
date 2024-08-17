from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

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

    return render(request, "website/home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("website:home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect("website:home")
    else:
        form = SignUpForm()
        return render(request, "website/register.html", {"form": form})

    return render(request, "website/register.html", {"form": form})


def record_detail(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "website/record.html", {"record": record})
    else:
        messages.success(request, "You must be logged in to view this page.")
    return redirect("website:home")
