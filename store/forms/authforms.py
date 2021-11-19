from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomerAuthForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Email")


class CustomerCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="First Name")
    last_name = forms.CharField(required=True, label="Last Name")

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if len(value.strip()) < 4:
            raise ValidationError("First Name must be 4 characters long....")
        return value.strip()
    
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if len(value.strip()) < 2:
            raise ValidationError("Last Name must be 2 characters long..")
        return value.strip()
       

    class Meta:
        model = User
        fields=['username','first_name','last_name']