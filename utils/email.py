from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(to , subject , context , template):

    try:
        html = render_to_string(template, context)
        plain_message = strip_tags(html)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=html)

    except:
        raise SMTPException('Sending Mail Error Occur.')