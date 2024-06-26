from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If the data entered is valid
            form.save() # Saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') # Succes message for created account
            return redirect('tracker-home') # Redirects the user to the main page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
