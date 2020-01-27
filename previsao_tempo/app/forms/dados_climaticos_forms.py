from django import forms
from ..models import DadosClimaticos

class DadosClimaticosForm(forms.ModelForm):
    class Meta:
        model = DadosClimaticos
        fields = ['data_medicao', 'hora_medicao', 'nascer_sol', 'por_sol', 'temperatura_atual', 'temperatura_minima',
                  'temperatura_maxima', 'velocidade_vento', 'umidade_relativa_ar', 'volume_chuva',
                  'detalhes', 'medicoes_cidade']