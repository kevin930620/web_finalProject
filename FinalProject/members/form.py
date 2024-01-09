from django import forms
from .models import Computer,CPUType,wishlist
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

# for filter
class FilterForm(forms.Form):
    cputype = forms.ModelChoiceField(
        queryset=CPUType.objects.all(),
        widget= forms.CheckboxSelectMultiple
    )

class add_wishForm(forms.Form):
    class Meta:
        computer =forms.ModelChoiceField(queryset=Computer.objects.all() )
        fields ='__all__' 


class hopeForm(forms.ModelForm):
    class Meta:
        model = wishlist
        fields =['user','computer']

        widget={
            'user':forms.Select(attrs={'readonly': 'readonly'}),
            'computer':forms.Select()
        } 
        labels = {
            'user':'使用者',
            'computer':'電腦'
        }


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']