from django.shortcuts import render
from .models import BANDAS_DATA

def lista_bandas(request):
    return render(request, 'bandas/bandas.html', {'bandas': BANDAS_DATA})

def lista_albumes(request, banda_id):
    banda = BANDAS_DATA.get(banda_id)
    if not banda:
        return render(request, 'bandas/error.html', {'mensaje': 'Banda no encontrada', 'bandas': BANDAS_DATA})
    
    return render(request, 'bandas/albumes.html', {
        'banda': banda,
        'banda_id': banda_id,
        'bandas': BANDAS_DATA
    })

def lista_canciones(request, banda_id, album_id):
    banda = BANDAS_DATA.get(banda_id)
    if not banda:
        return render(request, 'bandas/error.html', {'mensaje': 'Banda no encontrada', 'bandas': BANDAS_DATA})
    
    album = banda['albumes'].get(album_id)
    if not album:
        return render(request, 'bandas/error.html', {'mensaje': 'Álbum no encontrado', 'bandas': BANDAS_DATA})
    
    return render(request, 'bandas/canciones.html', {
        'banda': banda,
        'banda_id': banda_id,
        'album': album,
        'album_id': album_id,
        'bandas': BANDAS_DATA
    })
