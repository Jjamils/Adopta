from django.conf.urls.static import static
from django.db import models


class Perro(models.Model):
  codigo = models.AutoField(primary_key= True)
  nombre = models.CharField(max_length= 40)
  raza = models.CharField(max_length= 20)
  edad = models.CharField(max_length= 20)
  peso = models.CharField(max_length=20)
  color = models.CharField(max_length= 30)
  foto = models.ImageField(upload_to= 'images', null=True, blank= True)
  #Lista asignada a variable para crear opciones para escoger
  posee_entreno = [                             
    ('Entrenado', 'Entrenado(a)'),
    ('No entrenado', 'No entrenado(a)')
  ]

  entrenado = models.CharField(max_length= 20, choices= posee_entreno, default= 'Entrenado')
  sexos = [
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra')
  ]
  #La variable de opciones se pasa como parametro choices
  sexo = models.CharField(max_length= 20, choices= sexos, default= 'Macho')
  #Metodo para visualizar datos en admin
  def __str__(self): 
    return self.nombre



class Persona_adoptiva(models.Model):
  cedula = models.CharField(max_length=15, primary_key= True)
  nombre_completo = models.CharField(max_length= 60)
  primer_apellido = models.CharField(max_length= 30)
  segundo_apellido = models.CharField(max_length= 30)
  telefono = models.CharField(max_length= 15)
  direccion = models.CharField(max_length= 60)

  def __str__(self):
    return self.nombre_completo


class Adopcion(models.Model):
  numero_adopcion = models.AutoField(primary_key= True)
  fecha_adopcion = models.DateTimeField(auto_now_add= True)
  perro = models.ForeignKey(Perro, null= False, blank= False, on_delete=models.PROTECT)
  persona_adoptiva = models.ForeignKey(Persona_adoptiva, null= False, blank= False, on_delete=models.PROTECT)

  def __str__(self):
    txt = "( {0} ) Fecha de adopcion: {1}"
    return txt.format (self.perro.nombre, self.fecha_adopcion.strftime('%A %d %m %Y %H:%M:%S'))


