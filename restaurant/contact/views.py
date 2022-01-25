from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, authenticate, AuthenticationForm
# Create your views here.

def Signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/account/login/')
    else:
        form = UserCreationForm()
    return render(request, 'account/singup.html', {'form': form})

def Login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/foods/')

    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def Logout_view(request):
    if request.method == 'POST':
        logout(request)
        #form = AuthenticationForm()
        return redirect('/account/login/')
