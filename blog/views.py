from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from taggit.models import Tag

# Create your views here.


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 10 
    

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"