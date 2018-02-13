from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import CcAccount
from . import bset
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

#@login_required(login_url='login') decoratore che rimanda alla rotta di login_url
#@login_required(login_url='login') decorator which redirect you to the login


def loginPage(request):
    if request.method == 'GET':  # show login form
        msg = ''
        if request.GET.get("msg") is not None:
            msg = request.GET.get("msg")
            context = {'msg': msg}
            return render(request, 'banqueting/login.html', context)
        elif request.method == 'POST':  # try to do a login
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return redirect('/login?msg=login errato')
    return redirect('/')


@login_required(login_url='/login')
def index(request):
    accounts = CcAccount.objects.all()
    context = {'accounts': accounts}
    return render(request, 'banqueting/index.html', context)


def modulo(request):
    context = {placeholder: 'value'}
    return render(request, 'banqueting/modulo.html', context)
