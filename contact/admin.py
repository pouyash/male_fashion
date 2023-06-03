from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from contact.models import Contact, Address, ContactSetting


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


@register(ContactSetting)
class ContactSettingAdmin(admin.ModelAdmin):
    list_display = ['id','title','title_red','text','is_active']
    list_editable = ('title','title_red','text','is_active',)

@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','title','phone','address','is_active']
    list_editable = ('title', 'phone','address', 'is_active',)