from django.contrib import admin
from django.contrib.admin import register

from about.models import OurTeam, Partner, Message, AboutImage, Question, About


@register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active']


@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'is_active']


@register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['our_team', 'name', 'image', 'is_active']


@register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'is_active']


@register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_active']


@register(About)
class AboutAdmin(admin.ModelAdmin):
    pass