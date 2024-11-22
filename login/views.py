from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import logout
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('signup')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use. Please choose another.")
            return redirect('signup')

        # Create the user if everything is valid
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect('signin')

    return render(request, "signup.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('message')  # Redirect to home or another desired page
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')  # Redirect back to signin on failure

    return render(request, "signin.html")

def message(request):
    return render(request, "homepage.html")

def logout_view(request):
    return redirect('home')

