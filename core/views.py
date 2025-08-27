from django.shortcuts import render,redirect
from .models import Student
from .forms import BioModelForm
def home(request):
    if request.method == "POST":
        form = BioModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume/')
        
        else:
            print("Please fill all the required fields.")

    forms = BioModelForm()
    context = {
        "bio_form" : forms
    }
    template = 'core/index.html'
    return render(request,template,context)
   

def resume(request):
    template = 'home/resume.html'
    return render(request,template)



