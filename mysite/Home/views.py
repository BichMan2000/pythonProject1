from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'pages/home.html')


def course(request):
    return render(request, 'pages/course.html')


def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')


def contact(request):
    return render(request, 'pages/contact.html')

def introduce(request):
    return render(request, 'pages/introduce.html')


def form_login(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'pages/form_login.html',{'form':form})
