from django.shortcuts import render
from django.template.context_processors import request

def home(request):
    context = {"title" : "Home"}
    return render(request, 'home/home.html', context)
