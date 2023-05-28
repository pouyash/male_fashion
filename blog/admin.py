from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from blog.models import Blog, Comment


@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['slug','is_active','short_description','user']
    list_editable = ['is_active','short_description']
    readonly_fields = ['user']
    prepopulated_fields = {
        'slug':('title',)
    }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()



@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','parent','text']