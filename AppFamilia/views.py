from django.shortcuts import render
from AppFamilia.models import Familia

# Create your views here.
def addfamily(request):
    dato = Familia(nombre=" Daniel",apellido="Olivar",nacimiento="1990-08-27",edad=32)
    dato.save()
    contexto = {
        "agregar":dato
    }
    return render(request,"agregar.html",contexto)

def verfamily(request):
    miembro1 = Familia.objects.all()
    contexto = {
        "ver":miembro1
    }
    return render(request,"vermifamilia.html",contexto)