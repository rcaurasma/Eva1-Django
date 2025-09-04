from django.shortcuts import render
from .models import BANDAS_DATA

# Views para el catálogo de bandas musicales

def lista_bandas(request):
    """Vista que muestra la lista de todas las bandas"""
    return render(request, 'bandas/bandas.html', {'bandas': BANDAS_DATA})

def lista_albumes(request, banda_id):
    """Vista que muestra los álbumes de una banda específica"""
    banda = BANDAS_DATA.get(banda_id)
    if not banda:
        return render(request, 'bandas/error.html', {'mensaje': 'Banda no encontrada', 'bandas': BANDAS_DATA})
    
    return render(request, 'bandas/albumes.html', {
        'banda': banda,
        'banda_id': banda_id,
        'albumes': banda['albumes'],
        'bandas': BANDAS_DATA
    })

def lista_canciones(request, banda_id, album_id):
    """Vista que muestra las canciones de un álbum específico"""
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
        'canciones': album['canciones'],
        'bandas': BANDAS_DATA
    })
