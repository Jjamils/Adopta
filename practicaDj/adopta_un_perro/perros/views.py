from django.shortcuts import redirect, render
from .models import Perro
from .forms import PerroForm

def home (request):
  total_perros = Perro.objects.all()
  context = {'total_perros' : total_perros}
  return render (request, 'perros/home.html', context)



def agregar(request):
  if request.method == "POST":
    form = PerroForm (request.POST)
    if form.is_valid():
      form.save()
      return redirect (to = 'adopta:home')
  else:
      form = PerroForm()
  context = {'form': form}
  return render (request, 'perros/agregar.html', context)



def editar (request, codigo):
  edit_perro = Perro.objects.get( codigo = codigo)
  if request.method == 'POST':
    form = PerroForm(request.POST, instance = edit_perro)
    if form.is_valid():
      form.save()
      return redirect( to = "adopta:home")
  else:
    form = PerroForm(instance = edit_perro)
  context = {'form': form}
  return render (request, 'perros/editar.html', context)



def eliminar (request, codigo):
  delete_perro = Perro.objects.get( codigo = codigo)
  delete_perro.delete()
  return redirect (to ='adopta:home')

