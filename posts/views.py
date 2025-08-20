from django.shortcuts import render,HttpResponse
from . models import Post

def post(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    template = 'posts/posts.html'
    return render(request,template,context)

def post_details(request,id):
    print(id)
    template = 'posts/post_details.html'
    return render(request,template)