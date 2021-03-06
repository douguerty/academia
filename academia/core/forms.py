from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser, Exercicio, Treinamento, LogAgua
from django.conf import settings
from academia.settings import BASE_DIR


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


class ExercicioForm(forms.ModelForm):
    exercicio = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Exercicio'
            }
        )
    )

    musculo = forms.ChoiceField(
        choices=settings.MUSCULO_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Exercicio
        fields = ['exercicio', 'musculo']


class TreinamentoForm(forms.ModelForm):
    def __init__(self, usuario, *args, **kwargs):
        super(TreinamentoForm, self).__init__(*args, **kwargs)
        self.usuario = usuario
        self.fields['exercicio'].queryset = Exercicio.objects.filter(usuario=self.usuario)

    def save(self, commit=True):
        treinamento = super(TreinamentoForm, self).save(commit=False)
        treinamento.usuario = self.usuario

        if commit:
            treinamento.save()
        
        return treinamento


    data = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Data: dd/mm/aaaa', 'type': 'date'
            }
        )
    )

    exercicio = forms.ModelChoiceField(queryset=Exercicio.objects.all(),
        label='',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    series = forms.IntegerField(required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Séries'
            }
        )
    )

    repeticao = forms.IntegerField(required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Repetições por série'
            }
        )
    )

    tempo = forms.CharField(required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Tempo gasto por série em minutos'
            }
        )
    )

    distancia = forms.CharField(required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Distancia percorrida em KM'
            }
        )
    )

    peso = forms.CharField(required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Carga em KG usado no exercicio'
            }
        )
    )

    class Meta:
        model = Treinamento
        fields = ['data', 'exercicio', 'series', 'repeticao', 'tempo', 'distancia', 'peso']

    
class AguaForm(forms.ModelForm):
    consumo_agua = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Consumo de água (em ML)'
            }
        )
    )

    class Meta:
        model = MyUser
        fields = ['consumo_agua']