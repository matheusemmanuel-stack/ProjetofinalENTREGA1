from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Corte
from .forms import AgendamentoForm

def home(request):
    return render(request, 'core/home.html')


def listar_cortes(request):
    cortes = Corte.objects.filter(ativo=True)

    return render(request, 'core/cortes.html', {
        'cortes': cortes
    })

def contato(request):
    return render(request, 'core/contato.html')

def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('agendamento')
    else:
        form = AgendamentoForm()

    return render(request, 'core/agendamento.html', {'form': form})