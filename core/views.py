from django.shortcuts import render
from .models import Corte


def home(request):
    return render(request, 'core/home.html')


def listar_cortes(request):
    cortes = Corte.objects.filter(ativo=True)

    return render(request, 'core/cortes.html', {
        'cortes': cortes
    })