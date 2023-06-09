from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

from blog.models import Blog


class CanEditBlogPermission(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        blog: Blog = get_object_or_404(Blog, id=self.kwargs['id'])
        return self.request.user.is_superadmin or self.request.user == blog.user



class BlogPermission(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superadmin or self.request.user.role == 1