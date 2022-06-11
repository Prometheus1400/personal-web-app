from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms

def home(request):
    
    context = {}
    return render(request, 'homepage/home.html', context=context)


def projects(request):
    
    context = {}
    return render(request, 'homepage/projects.html', context=context)


def resume(request):
    
    context = {}
    return render(request, 'homepage/resume.html', context=context)


def contact(request):
    
    context = {}
    context['form'] = forms.contactForm()
    return render(request, 'homepage/contact.html', context=context)

def submit_contact(request):
    try:
        print(request)
        return HttpResponseRedirect('/contact/')
    except:
        # TODO: add error path
        return HttpResponseRedirect('/contact/')

