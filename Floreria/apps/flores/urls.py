from django.urls import path
from .views import crearFlor

urlpatterns = [
    path('crear_flor/',crearFlor, name = 'crear_flor')
    
    


]