from profiles.models import Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms.widgets import EmailInput, PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={'placeholder':'Username',
            'class':'form-control'
            }
         ))
    password=forms.CharField(
        widget=PasswordInput(
            attrs={'placeholder':'Mot de passe',
            'class':'form-control'
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=TextInput(attrs={
            'palceholder':'Prenom',
            'class':'form-control'
            }
        ))
    last_name = forms.CharField(
        widget=TextInput(attrs={
            'palceholder':'Nom',
            'class':'form-control'
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mot de passe",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Vérification mot de passe",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')