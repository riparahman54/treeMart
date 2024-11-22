from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile
from django import forms
from django.contrib.auth.decorators import login_required

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user, is_normal_user=True)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'message.html')
    else:
        return render(request, 'index.html')