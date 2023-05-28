from django import forms


class CommentForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(), label='Email')
    name = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Comment ... '
    }))