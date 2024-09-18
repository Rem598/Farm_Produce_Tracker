# produce/forms.py
from django import forms
from .models import Crop, Yield, Sale
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'type', 'planting_date']

class YieldForm(forms.ModelForm):
    class Meta:
        model = Yield
        fields = ['crop', 'date', 'amount']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['crop', 'date', 'quantity_sold', 'revenue']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    pass
