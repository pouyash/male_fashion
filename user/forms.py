from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,min_length=5,label='username',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    firstname = forms.CharField(max_length=100,label='firstname',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    lastname = forms.CharField(max_length=100,label='lastname',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }),label='Email')
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }), max_length=100,min_length=8)

    confirm_password = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }), max_length=100,min_length=8)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('password and confirm password is not equal.')




class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))