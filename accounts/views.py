from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm
from .models import Profile
from django import forms
from django.contrib.auth.decorators import login_required
#
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             Profile.objects.create(user=user, is_normal_user=True)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Save the user first

            # Create a profile for the new user
            Profile.objects.create(user=user, is_normal_user=True)
            login(request, user)  # Log the user in automatically
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if request.user.is_superuser:
        return render(request, 'homepage.html', {
        'profile': profile,
        'user_type': profile.get_user_type_display()  # This will show "Admin", "Seller", or "Buyer"
    })
    else:
        return render(request, 'index.html', {'profile': profile})