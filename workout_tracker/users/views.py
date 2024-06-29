from django.shortcuts import render, redirect
from django.contrib import messages # Import messages shown on the app (success msg, etc..)
from django.contrib.auth.decorators import login_required # Imports login required function
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # Imports our custom forms
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
    if request.method == 'POST':
        
        # We add instances to the forms so they are populated with the current logged in user's info
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        # Checks if both forms have valid data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    # We create a dictionary with our forms to send them to the html so we can use them there
    context = { 
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)
