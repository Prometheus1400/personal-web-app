from django.shortcuts import render

def home(request):
    
    context = {}
    return render(request, 'homepage/home.html', context=context)


def projects(request):
    
    context = {}
    return render(request, 'homepage/projects.html', context=context)


def resume(request):
    
    context = {}
    return render(request, 'homepage/resume.html', context=context)