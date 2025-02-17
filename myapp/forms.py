from django import forms

from myapp.models import Customer,User

from django.contrib.auth.forms import UserCreationForm




class CustomerForm(forms.ModelForm):

    class Meta:

        model=Customer

        fields=[
            "name",
            "email",
            "phone",
            "address"
        ]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] 

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter e-mail'}))