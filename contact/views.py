import sweetify
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views import View

from contact.forms import ContactModelForm
from contact.models import Contact, ContactSetting, Address


class ContactView(View):
    def get(self,request):
        contact_setting:ContactSetting = ContactSetting.objects.filter(is_active=True).last()
        address:Address = Address.objects.filter(is_active=True)
        form = ContactModelForm()
        context = {
            'form': form,
            'contact_setting': contact_setting,
            'address': address,
        }
        return render(request, 'contact/contact.html', context)


    def post(self, request:HttpRequest):
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # message = form.cleaned_data.get('message')
            # Contact.objects.create(name=name, email=email, message=message)
            sweetify.success(request, 'Your Message Send Successfully! Thanks For Your Contribution')

        else:
            sweetify.error(request, 'Error Occurred')
        context = {
            'form': form,
        }
        return render(request, 'contact/contact.html', context)


