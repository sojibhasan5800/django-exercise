from django import forms

class contatfrom(forms.Form):
    # name = forms.CharField(label="User Name")
    # email= forms.EmailField(label="Email")
    # age = forms.IntegerField()
    # birthday = forms.DateField()
    CHOICE = [('S','serach'),('R','arjo')]
    our = forms.ChoiceField(choices=CHOICE)
    # select = forms.ChoiceField(choices=CHOICE)
    selected = forms.MultipleChoiceField(choices=CHOICE)
    