from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone

def publicacion_lista(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})
