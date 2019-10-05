# django
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# local django
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'celular', 'fixo']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    fullname = forms.CharField(label="Primeiro nome")

    class Meta:
        model = User
        fields = ('cpf', 'username', 'fullname',
                  'last_name', 'email', 'celular', 'fixo')
