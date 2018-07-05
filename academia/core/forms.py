from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome'
            }
        )
    )
    last_name = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Sobrenome'
            }
        )
    )
    email = forms.EmailField(label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Email'
            }
        )
    )

    password1 = forms.CharField(label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Senha'
            }
        )
    )

    password2 = forms.CharField(label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']