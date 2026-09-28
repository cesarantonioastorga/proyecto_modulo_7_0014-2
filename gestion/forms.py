from django import forms
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'email',
            'telefono'
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': 'Nombre completo',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': 'correo@ejemplo.com',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': '+56 9 1234 5678',
                }
            ),
        }
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control aw-input',
                'placeholder':'Usuario',
                'autofocus': True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control aw-input',
                'placeholder': 'Contrasena',
            }
        )
    )