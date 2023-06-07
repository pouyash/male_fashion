from django.contrib import admin
from django.contrib.admin import register

from site_settings.models import Slider


@register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['header','product','is_active']
    ordering = ('-id',)
