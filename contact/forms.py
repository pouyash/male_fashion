from django import forms
from captcha.fields import CaptchaField

from contact.models import Contact


class ContactModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"
        required = "__all__"
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
        }

        widgets = {
            'name':forms.TextInput(attrs={
                'placeholder': 'My Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@mail.com'
            })
        }

    def save(self, commit=True):
        instance = super(ContactModelForm, self).save(commit=False)
        # Exclude field3 from being saved to the database
        exclude_fields = ['captcha']
        for field in exclude_fields:
            if field in self.cleaned_data:
                setattr(instance, field, None)
        if commit:
            instance.save()

        return instance