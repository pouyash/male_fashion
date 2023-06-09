from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog


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


class BlogForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'is_active', 'description', 'image']
        required = ['title', 'short_description', 'description', 'image', 'is_active']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

