from django.shortcuts import render,HttpResponse

# Create your views here.

def post(request):
    template = 'home/posts.html'
    return render(request,template)

def post_details(request):
    return HttpResponse("<h1>This is post details page.</h1>")