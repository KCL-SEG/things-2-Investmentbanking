"""Forms of the project."""
from django import forms
from django.contrib.auth import authenticate
from .models import Thing

# Create your forms here.
# Exercise 1: Things form
# The project includes a nearly empty file called things/forms.py. In this file, define a form called ThingForm, that contains the fields name, description, and quantity, but not created_at.

# The form must accept valid inputs for Thing and reject invalid input for Thing.

# The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput.

class ThingForm(forms.ModelForm):
    # description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 0, 'max': 50}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


