from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)
