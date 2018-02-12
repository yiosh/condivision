from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    variabile = 'YYGUFU'
    context = {'N':variabile}
    return render(request, 'calderoni/index.html', context)

def modulo(request):
    context = {'placeholder':'value'}
    return render(request, 'banqueting/modulo.html', context)
