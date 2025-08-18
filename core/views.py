from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    template = 'home/index.html'
    return render(request,template)

def resume(request):
    template = 'home/resume.html'
    return render(request,template)



