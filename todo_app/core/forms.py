from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'w-full p-2 border border-gray-200 rounded-xl',
                'placeholder':"Your Username"
            }),

            'email':forms.EmailInput(attrs={
                'class':'w-full p-2 border border-gray-200 rounded-xl',
                'placeholder':"Your Email"
            }),
        }
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full p-2 border border-gray-200 rounded-xl',
        'placeholder':"Your Password"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full p-2 border border-gray-200 rounded-xl',
        'placeholder':"Repeat Password"
    }))


