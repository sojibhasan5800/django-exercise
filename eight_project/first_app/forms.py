from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields =   fields = ['username', 'first_name', 'last_name', 'email']