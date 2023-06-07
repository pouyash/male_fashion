from django import forms
from django.core.exceptions import ValidationError


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Your Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }), label='confirm_password')


    def clean_confirm_password(self):
        if self.cleaned_data.get('password') == self.cleaned_data.get('confirm_password'):
            return self.cleaned_data.get('confirm_password')
        else:
            return ValidationError('password and confirm password is not equal')