from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Proyecto4.forms import CreacionLanguagesFormulario, CreacionFrameworkFormulario, BusquedaLanguagesFormulario, ActualizarLanguagesFormulario,ActualizarFrameworkFormulario
from Proyecto4.models import Language, Framework

# Create your views here.

def Inicio(request):
    
    return render(request,"inicio/Inicio.html")

def Languages(request):
    # nombre_buscar = request.GET.get('nombre')
    
    # if nombre_buscar:
    #     listado_de_languages = Language.objects.filter(nombre__icontains= nombre_buscar.lower())
    # else:
    #     listado_de_languages = Language.objects.all()
    form_Busqueda = BusquedaLanguagesFormulario(request.GET)
    if form_Busqueda.is_valid():
        nombre_buscar = form_Busqueda.cleaned_data.get("nombre")
        listado_de_languages = Language.objects.filter(nombre__icontains= nombre_buscar.lower())
        
    form_Busqueda = BusquedaLanguagesFormulario()
    return render(request, "inicio/Languages.html", {"busqueda":form_Busqueda,'languages': listado_de_languages})


def Frameworks(request):
    nombre_buscar = request.GET.get("nombre")
    
    if nombre_buscar:
        listado_de_frameworks = Framework.objects.filter(nombre__icontains= nombre_buscar.lower())
    else:
        listado_de_frameworks = Framework.objects.all()
    
    return render(request, "inicio/Frameworks.html", {"frameworks": listado_de_frameworks})

@login_required
def Creacion_Languages(request):
    
    if request.method == "POST":
        formularioLanguages = CreacionLanguagesFormulario(request.POST)
        if formularioLanguages.is_valid():
            info_limpiaLanguages = formularioLanguages.cleaned_data
            
            print(info_limpiaLanguages)
            
            nombre = info_limpiaLanguages.get("nombre")
            creador = info_limpiaLanguages.get("creador")
            version = info_limpiaLanguages.get("version")
            descripcion = info_limpiaLanguages.get("descripcion")
            print(nombre)
            
            languages = Language(nombre = nombre , creador = creador , version = version , descripcion = descripcion)
             
            languages.save()
            return redirect(Languages)
        else: 
            return render(request,"", {"formularioLanguages": formularioLanguages})
    formularioL = CreacionLanguagesFormulario()
    return render(request,"inicio/CreacionLanguages.html", {"formularioLl": formularioL})       
    
@login_required
def Creacion_Frameworks(request):
    
    if request.method == "POST":
        formularioFramework = CreacionFrameworkFormulario(request.POST)
        if formularioFramework.is_valid():
            info_limpiaFramework = formularioFramework.cleaned_data
            # AGARRO EL DATO DEL FORM Y LO GUARDO EN VARIABLE
            nombre = info_limpiaFramework.get("nombre")
            languages = info_limpiaFramework.get("languages")
            descripcion = info_limpiaFramework.get("descripcion")
            # DONDE DIGA TAL COSA EN EL MODELO REMPLAZALO POR TAL VARIABLE. SAVE GUARDA EN EL MODELO
            framework = Framework(nombre = nombre , languages = languages , descripcion = descripcion)
            framework.save()
            # REDIRIGIR A LA VIEW INICIO
            return redirect(Frameworks)
        else:
            # SI NO ES VALIDO EL FORMULARIO, SE MUESTRA EL ERROR PERO NO ME ESTA FUNCIONANDO- ARREGLAR -
            return render(request, "", {"formularioFramework": formularioFramework}) 
    formularioF = CreacionFrameworkFormulario()
    # LE PASO EL FORMULARIO VACIO ABAJO, PORQUE LA PRIMER VISTA VIENE POR GET
    return render(request,"inicio/CreacionFrameworks.html", {"formularioFf": formularioF})

@login_required
def Eliminar_Language(request,language_id):
    language_a_elminar = Language.objects.get(id=language_id)
    language_a_elminar.delete()
    
    return redirect(Languages)

@login_required
def Eliminar_Framework(request,framework_id):
    framework_a_elminar = Framework.objects.get(id=framework_id)
    framework_a_elminar.delete()
    
    return redirect(Frameworks)

@login_required
def Actualizar_Language(request,language_id):
    language_a_actualizar = Language.objects.get(id=language_id)
    
    if request.method == "POST":
        formulario = ActualizarLanguagesFormulario(request.POST)
        if formulario.is_valid():
            actualizado = formulario.cleaned_data
            
            language_a_actualizar.nombre = actualizado.get("nombre")
            language_a_actualizar.creador = actualizado.get("creador")
            language_a_actualizar.version = actualizado.get("version")
            language_a_actualizar.descripcion = actualizado.get("descripcion")
            
            language_a_actualizar.save()
            return redirect(Languages)
            
    formulario = ActualizarLanguagesFormulario(initial={"nombre" : language_a_actualizar.nombre, "creador" : language_a_actualizar.creador,"version" : language_a_actualizar.version, "descripcion" : language_a_actualizar.descripcion })
    
    return render(request,"inicio/ActualizarLanguages.html", {"formulario":formulario})

@login_required
def Actualizar_Framework(request,framework_id):
    framework_a_actualizar = Framework.objects.get(id=framework_id)
    
    if request.method == "POST":
        formulario = ActualizarFrameworkFormulario(request.POST)
        if formulario.is_valid():
            actualizado = formulario.cleaned_data
            
            framework_a_actualizar.nombre = actualizado.get("nombre")
            framework_a_actualizar.languages = actualizado.get("languages")
            framework_a_actualizar.descripcion = actualizado.get("descripcion")
            
            framework_a_actualizar.save()
            return redirect(Frameworks)
        else:
            return redirect(request, "inicio/ActualizarFrameworks.html", {"formulario": formulario})
        
    formulario = ActualizarFrameworkFormulario(initial={"nombre" : framework_a_actualizar.nombre,"languages" : framework_a_actualizar.languages,"descripcion" : framework_a_actualizar.descripcion})
    return render(request,"inicio/ActualizarFrameworks.html", {"formulario": formulario})

def Detalle_Language(request, language_id):
    language = Language.objects.get(id=language_id)
    return render(request,"inicio/DetalleLanguages.html", {"language": language})

def Detalle_Framework(request, framework_id):
    framework = Framework.objects.get(id=framework_id)
    return render(request,"inicio/DetalleFrameworks.html", {"framework": framework})
    
def About(request):
    
    return render(request,"inicio/About.html")

def Contact(request):
    
    return render(request,"inicio/Contact.html")

