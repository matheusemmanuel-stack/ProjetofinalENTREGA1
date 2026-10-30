from django import forms
from django.utils import timezone
from .models import Agendamento
from datetime import datetime, timedelta


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_cliente', 'corte', 'data', 'horario']

        labels = {
            'nome_cliente': 'Nome completo',
            'corte': 'Corte desejado',
            'data': 'Data do agendamento',
            'horario': 'Horário desejado',
        }

        widgets = {
            'nome_cliente': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome completo'
            }),
            'corte': forms.Select(),
            'data': forms.DateInput(attrs={
                'type': 'date'
            }),
            'horario': forms.TimeInput(attrs={
                'type': 'time'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        horario = cleaned_data.get('horario')
        corte = cleaned_data.get('corte')

        # Mantém validações anteriores de data/horário passado...

        if data and horario and corte:
            inicio_novo = datetime.combine(data, horario)
            fim_novo = inicio_novo + timedelta(minutes=corte.duracao)

            agendamentos = Agendamento.objects.filter(data=data).exclude(pk=self.instance.pk)

            for agendamento in agendamentos:
                inicio_existente = datetime.combine(agendamento.data, agendamento.horario)
                fim_existente = inicio_existente + timedelta(minutes=agendamento.corte.duracao)

                # Regra de interseção de intervalos
                if inicio_novo < fim_existente and fim_novo > inicio_existente:
                    self.add_error(
                        'horario',
                        'Esse horário não está disponível. Escolha outro horário.'
                    )
                    break

        return cleaned_data