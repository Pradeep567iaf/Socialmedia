from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'homepage.html') 

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html') 
