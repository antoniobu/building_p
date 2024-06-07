from django.contrib.auth.models import User
from django.forms import *
from django import forms



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Нікнейм'}),
            
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Електронна пошта'})
            
        }
class LoginForm(forms.Form):
    username = forms.CharField(label='Ваш нікнейм', widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Нікнейм'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))



class MakeOrder(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
