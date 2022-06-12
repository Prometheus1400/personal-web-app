from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('resume/', views.resume, name="resume"),
    path('contact/', views.contact, name="contact"),
    path('submit_contact/', views.submit_contact),
]