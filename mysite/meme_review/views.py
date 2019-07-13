from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Post, Comment

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'meme_review/templates/home.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[0:]
