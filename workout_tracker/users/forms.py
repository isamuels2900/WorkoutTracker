from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile # We must import Profile to be able to access the user's PFP

# This form inherits from the UserCreationForm to add extra fields to that form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    # Class meta handles the configuration of the form
    class Meta:
        model = User # Model form interacts with
        fields = ['username', 'email', 'password1', 'password2'] # Indicates the form fields and the order
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    # Class meta handles the configuration of the form
    class Meta:
        model = User # Model form interacts with
        fields = ['username', 'email'] # Indicates the form fields and the order
        
# This class allows us to change the user profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']