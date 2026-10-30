from django.shortcuts import render, redirect
from .models import Corte
from django.contrib import messages
from .forms import AgendamentoForm

def home(request):
    return render(request, 'core/home.html')


def listar_cortes(request):
    cortes = Corte.objects.filter(ativo=True)

    return render(request, 'core/cortes.html', {
        'cortes': cortes
    })

def solicitar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Agendamento solicitado com sucesso!'
            )

            return redirect('agendamento')
    else:
        form = AgendamentoForm()

    return render(
        request,
        'core/agendamento.html',
        {'form': form}
    )