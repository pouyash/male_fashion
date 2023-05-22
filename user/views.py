import time
import sweetify
from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from user.forms import RegisterForm, LoginForm
from user.models import User
from utils.email import send_email


class RegisterView(View):
    def get(self,request:HttpRequest):
        forms = RegisterForm()
        context = {
            'forms':forms,
        }
        return render(request,'user/register.html',context)

    def post(self,request:HttpRequest):
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            email = forms.cleaned_data.get('email')
            first_name = forms.cleaned_data.get('firstname')
            last_name = forms.cleaned_data.get('lastname')
            user = User.objects.create(
            email = email,
            username = username,
            is_active=False,
            activate_code = get_random_string(length=72) + str(time.time())[-10],
            first_name=first_name,
            last_name=last_name,
            role=2
            )
            user.set_password(password)
            user.save()

            context = {
                'code':user.activate_code,
            }
            send_email(to=user.email, subject='Activate Email', context=context, template='email/active.html')

            sweetify.success(request,'Account Created Successfully. Please Active It.')

            return redirect(reverse('home'),request)

        else:
            context = {
                'forms': forms
            }
            sweetify.error(request, 'Problem Occur!')
            return render(request, 'user/register.html', context)



class LoginView(View):
    def get(self,request:HttpRequest):
        forms = LoginForm()
        context = {
            'forms':forms,
        }
        return render(request,'user/login.html',context)

    def post(self,request:HttpRequest):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=email).first()
            if user:
                if user.check_password(forms.cleaned_data.get('password')):
                    if user.is_active:
                        login(request,user)
                        sweetify.success(request,'You Logged in Successfully!')
                        return redirect(reverse('home'))
                    else:
                        sweetify.error(request, 'Your Account is not Active')
                        return render(request, 'user/login.html', context={'forms': forms})
                else:
                    sweetify.error(request,'Your Password is not True or Your email Not Found!')
                    return render(request,'user/login.html',context={'forms':forms})
            else:
                sweetify.error(request, 'Your Password is not True or Your email Not Found!')
                return render(request, 'user/login.html', context={'forms': forms})

        return render(request,'user/login.html',context={'forms':forms})



class ActiveUser(View):

    def get(self,request,code):
        user = User.objects.filter(activate_code__iexact=code).first()
        user.is_active = True
        user.activate_code = get_random_string(72) + str(time.time())[-10]
        user.save()
        sweetify.success(request, 'User Activated !')
        return redirect(reverse('home'),request)
