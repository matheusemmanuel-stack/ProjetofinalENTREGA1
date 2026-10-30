from django import forms
from django.utils import timezone
from .models import Agendamento


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

        if data and horario:
            agora = timezone.localtime()
            data_atual = timezone.localdate()

            if data < data_atual:
                self.add_error(
                    'data',
                    'Não é possível agendar para uma data passada.'
                )

            elif data == data_atual and horario <= agora.time().replace(
                second=0,
                microsecond=0
            ):
                self.add_error(
                    'horario',
                    'Escolha um horário futuro.'
                )

        return cleaned_data