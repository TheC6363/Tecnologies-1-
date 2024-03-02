from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import Registration,EditarPerfil

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        print("pasando por aca")       
        formulario =AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            contra = formulario.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contra)
            
            django_login(request,user)
            
            return redirect("inicio")
    return render(request,"cuentas/login.html", {"formulario_login" : formulario})
        
def registro(request):
    formulario = Registration()
    
    if request.method == "POST":
        formulario = Registration(request.POST)
        if formulario.is_valid():
            print("PORFAVOR")
            formulario.save()
            return redirect("login")
   
    return render(request,"cuentas/registro.html", {"formulario_registro": formulario})

def editar_Perfil(request):
    formulario = EditarPerfil(instance=request.user)
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=request.user)
        
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
        
    return render(request,"cuentas/editar.html",{"formulario_perfil": formulario})