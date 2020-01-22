from django.shortcuts import render
from . models import Projects
# Create your views here.


def home(request):
    projects = Projects.objects.all().order_by('-title')
    return render(request, 'portfolio/home.html', {'projects': projects})


def about(request):
    return render(request, 'portfolio/about.html')
