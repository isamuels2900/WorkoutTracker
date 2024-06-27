from django.shortcuts import render, redirect
from django.contrib import messages # Import messages shown on the app (success msg, etc..)
from django.contrib.auth.decorators import login_required # Imports login required function
from .forms import UserRegisterForm # Imports our custom form for user registration
from django.contrib.auth import logout # Import logout for logout function

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If the data entered is valid
            form.save() # Saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!') # Succes message for created account
            return redirect('login') # Redirects the user to the main page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required # Users need to be logged in to view the profile page
def profile(request):
    return render(request, 'users/profile.html')
