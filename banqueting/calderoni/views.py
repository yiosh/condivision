from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required(login_url='/login')
def index(request):
    variabile = 'YYGUFU'
    context = {'N':variabile}
    return render(request, 'calderoni/index.html', context)

def modulo(request):
    context = {'placeholder':'value'}
    return render(request, 'banqueting/modulo.html', context)

def loginPage(request):
    if request.method == 'GET': #show login form
        msg = ''
        if request.GET.get("msg") is not None : msg = request.GET.get("msg")
        context = {'msg' : msg}
        return render(request, 'banqueting/login.html', context)
    elif request.method == 'POST': #try to do a login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None :
            login(request, user)
        else:
            return redirect('/login?msg=login errato')
    return redirect('/')
