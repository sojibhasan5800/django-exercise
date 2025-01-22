from django import forms
from django.core import validators
class contatfrom(forms.Form):
    # names = forms.CharField(label="User Name" , widget= forms.TextInput , validators=[validators.MaxLengthValidator(10, message="place check 10 len")])
    # email= forms.EmailField(label="Email", widget=forms.EmailInput, validators=[validators.EmailValidator (message='valid email')])
    # file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['jpeg','png'])])
    # # age = forms.IntegerField()
    # # CHOICE = [('S','serach'),('R','arjo')]
    # # birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    # # appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # # our = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)

    # # selected = forms.MultipleChoiceField(choices=CHOICE, widget=forms.CheckboxSelectMultiple)

    # # def clean(self):
    # #     cleaned_data = super().clean()
    # #     valname = cleaned_data.get('names')
    # #     valemail = cleaned_data.get('email')
    # #     if valname and len(valname) < 10:
    # #         raise forms.ValidationError("name minums 10 char")
    # #     if valemail and not valemail.endswith('.com'):
    # #         raise forms.ValidationError("place provided .com")
    password = forms.CharField(widget=forms.PasswordInput , required= False)
    re_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data= super().clean()
        first = self.cleaned_data.get('password')
        sec = self.cleaned_data.get('re_password')
        if first != sec :
            raise forms.ValidationError("password are not match")