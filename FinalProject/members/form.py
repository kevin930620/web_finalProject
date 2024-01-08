from django import forms
from .models import Computer,CPUType
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

# for filter
class FilterForm(forms.Form):
    cputype = forms.ModelChoiceField(
        queryset=CPUType.objects.all(),
        widget= forms.CheckboxSelectMultiple
    )
