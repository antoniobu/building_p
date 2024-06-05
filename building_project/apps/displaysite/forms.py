from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

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