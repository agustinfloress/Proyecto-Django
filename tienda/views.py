from django.shortcuts import render
from .models import Producto, CategoriaProd, Genero

def tienda(request):
    categorias_hombres = CategoriaProd.objects.filter(genero=Genero.MASCULINO)
    categorias_mujeres = CategoriaProd.objects.filter(genero=Genero.FEMENINO)
    categorias_ninos = CategoriaProd.objects.filter(genero=Genero.NINOS)

    context = {
        'categorias_hombres': categorias_hombres,
        'categorias_mujeres': categorias_mujeres,
        'categorias_ninos':categorias_ninos
    }
    return render(request, 'tienda/tienda.html', context)