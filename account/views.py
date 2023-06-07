from datetime import datetime

import sweetify
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views import View

from account.forms import ChangePasswordForm
from user.models import User
from utils.email import send_email


@method_decorator(login_required, name='dispatch')
class AccountMainView(View):

    def get(self, request: HttpRequest):
        context = {

        }
        return render(request, 'account/main.html', context)

@method_decorator(login_required, name='dispatch')
class ChangePasswordEmail(View):
    def get(self, request: HttpRequest):
        return render(request, 'account/change_password_email.html')

    def post(self, request: HttpRequest):
        user: User = request.user
        to = user.email
        template = 'email/change_password.html'
        code = user.activate_code
        context = {
            'code': code,
        }
        send_email(to=to, template=template, context=context, subject='Change Password')
        sweetify.success(request, 'Email Send Successfully!')
        return redirect(reverse('change_password_email'))

@method_decorator(login_required, name='dispatch')
class Change_password(View):
    def get(self, request, code):
        user = get_object_or_404(User, activate_code__iexact=code)
        return redirect(reverse('change_password_post'))


@method_decorator(login_required, name='dispatch')
class Change_password_post(View):
    def get(self, request):
        form = ChangePasswordForm()
        context = {
            'form': form,
        }
        return render(request, 'account/change_password.html', context)
    def post(self, request, ):
        user: User = request.user
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.activate_code = get_random_string(length=72) + str(datetime.now())
            user.save()
            logout(request)
            return redirect(reverse('login'))

        context = {
            'form': form,
        }
        sweetify.error(request, 'Error Occur.')
        return render(request, 'account/change_password.html', context)
