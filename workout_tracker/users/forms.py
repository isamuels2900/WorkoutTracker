from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile # We must import Profile to be able to access the user's PFP
from tracker.models import TemplateExercise, Exercise, Template
# Imports for the layout of the crispy forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


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
        
# Classes for the add exercise form
class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name  # Adjust this if your field name is different
    
class AddExerciseForm(forms.ModelForm):
    template = CustomModelChoiceField(queryset=Template.objects.none())
    exercise = CustomModelChoiceField(queryset=Exercise.objects.all())
    
    class Meta:
        model = TemplateExercise
        fields = ['template', 'exercise', 'sets', 'reps']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['template'].queryset = Template.objects.filter(author=user)
            