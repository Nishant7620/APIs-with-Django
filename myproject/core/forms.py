from django import forms
from django.core.validators import RegexValidator

class ProcessForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[RegexValidator(regex='^[a-zA-Z]*$',message='Name should contain only alphabetic characters')],widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
    salary = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={'class':'form-control'}))

class JokesForm(forms.Form):
    count = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
