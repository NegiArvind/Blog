from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogPostListView(ListView):
    model=Post
    template_name='home.html'

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class PostCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__' # all fields will be shown in new form

class PostUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']

class PostDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    # Instead of using reverse here we use reverse_lazy because we only want to redirect the user to home page
    # only after successfull deletion of post. 
    success_url=reverse_lazy('blog:home') # it will redirect you to the home page after successful deletion.
