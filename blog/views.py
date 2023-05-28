from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Blog, Comment


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 1


# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'blog'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogDetailView, self).get_context_data()
#         context['form'] = CommentForm()
#         return context


class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blog.objects.filter(slug__iexact=slug).first()
        comments = Comment.objects.filter(blog=blog, parent=None, is_active=True)
        comments_all_count = Comment.objects.filter(is_active=True, blog=blog)
        form = CommentForm()
        context = {
            'form': form,
            'blog': blog,
            'comments': comments,
            'count':comments_all_count
        }
        return render(request, 'blog/blog_detail.html', context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        blog = Blog.objects.filter(slug__iexact=slug).first()
        comments_all_count = Comment.objects.filter(is_active=True, blog=blog)
        if request.user.is_authenticated:
            text = request.POST.get('text')
            Comment.objects.create(
                name=request.user.username,
                email=request.user.email,
                text=text,
                blog=blog,
            )

        else:
            if form.is_valid():
                text = form.cleaned_data.get('text')
                email = form.cleaned_data.get('email')
                name = form.cleaned_data.get('name')
                Comment.objects.create(
                    name=name,
                    email=email,
                    text=text,
                    blog=blog,
                )
        comments = Comment.objects.filter(blog=blog, parent=None, is_active=True)
        context = {
            'blog': blog,
            'form': form,
            'comments': comments,
            'count': comments_all_count
        }
        return render(request, 'blog/blog_detail.html', context)
