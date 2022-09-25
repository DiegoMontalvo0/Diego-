from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('/admin')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')