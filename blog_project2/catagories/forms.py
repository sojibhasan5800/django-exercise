from django import forms
from .models import catagori

class catagory_form(forms.ModelForm):
    class Meta:
        model = catagori
        fields = '__all__'