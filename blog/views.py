from django.shortcuts import  HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm

from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


## for testing purpose
def test(request):
    return HttpResponse('this is test route')


class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class BlogListView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'

class UserBlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/user_blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('user_blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('home')

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('home')

