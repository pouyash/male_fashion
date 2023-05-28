from django.contrib import auth
from django.db import models
from django.utils.text import slugify

from user.models import User


class Blog(models.Model):
    title = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(max_length=600,db_index=True,unique=True)
    short_description = models.TextField(max_length=800)
    description = models.TextField()
    image = models.ImageField(upload_to='blog')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # self.user = kwargs.get('user')
        super(Blog, self).save()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment', null=True, blank=True)
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('Comment', related_name='comment', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    text = models.TextField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email