from django.urls import path
from .import views

#Importacionses para trabajar imagenes
from django.conf import settings
from django.conf.urls.static import static



app_name = 'adopta'
urlpatterns = [ 
  path('', views.home, name = 'home'),
  path('agregar/', views.agregar, name = 'agregar'),
  path('editar/<codigo>/', views.editar, name = 'editar'),
  path('eliminar/<int:codigo>/', views.eliminar, name = 'eliminar'),
]

#URL para las imagenes
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)