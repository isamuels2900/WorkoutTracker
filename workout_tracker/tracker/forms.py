from django import forms

# This form inherits from the UserCreationForm to add extra fields to that form
class one_rep_max_calculator_form(forms.Form):
    weight = forms.FloatField()
    reps = forms.IntegerField()