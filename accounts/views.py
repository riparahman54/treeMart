from django.contrib import messages

from django.shortcuts import render, redirect



# Create your views here.



from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate



from .forms import UserRegistrationForm

from .models import Profile

from django import forms

from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User

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



@login_required

def view_profile(request):

    try:

        profile = Profile.objects.get(user=request.user)

    except ObjectDoesNotExist:

        profile = None  # In case the profile does not exist yet



    return render(request, 'view_profile.html', {'profile': profile, 'user': request.user})





@login_required

def edit_profile(request):
    profile = request.user.profile  # Assuming one-to-one relationship with User
    if request.method == 'POST':
        # Update user information (username and email)
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username != request.user.username and User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('edit_profile')

        if email != request.user.email and User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!")
            return redirect('edit_profile')

        # Update the user's details
        request.user.username = username
        request.user.email = email
        request.user.save()

        # Update profile details
        profile.bio = request.POST.get('bio')
        profile.location = request.POST.get('location')

        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()

        messages.success(request, "Your profile has been updated successfully!")
        return redirect('view_profile')  # Redirect to profile page or any desired location
    return render(request, 'edit_profile.html', {'profile': profile, 'user': request.user})



@login_required

def view_profile(request):

    try:

        profile = Profile.objects.get(user=request.user)

    except ObjectDoesNotExist:

        profile = None  # Handle case where profile does not exist



    return render(request, 'view_profile.html', {'profile': profile, 'user': request.user})