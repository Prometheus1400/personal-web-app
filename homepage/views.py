import email
from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import forms, models

def home_redirect(request):
    
    return redirect('/home/')

def home(request):
    
    context = {}
    return render(request, 'homepage/home.html', context=context)


def about(request):
    
    context = {}
    return render(request, 'homepage/about.html', context=context)


def projects(request):
    
    context = {}
    return render(request, 'homepage/projects.html', context=context)


def resume(request):
    
    context = {}
    return render(request, 'homepage/resume.html', context=context)


def contact(request):
    context = {}

    if request.method == 'POST':
        form = forms.contactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = models.Person(
                email=data['email'], 
                organization=data['organization'], 
                message=data['message'], 
                reason=form.reason_list[int(data['reason'])][1])
            p.save()

            context['thanks'] = True
            return render(request, 'homepage/contact.html', context=context)
    else:
        context['form'] = forms.contactForm()
        return render(request, 'homepage/contact.html', context=context)

def submit_contact(request):
    try:
        print(request)
        return HttpResponseRedirect('/contact/')
    except:
        # TODO: add error path
        return HttpResponseRedirect('/contact/')

