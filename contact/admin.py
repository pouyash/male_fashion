from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from contact.models import Contact


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']