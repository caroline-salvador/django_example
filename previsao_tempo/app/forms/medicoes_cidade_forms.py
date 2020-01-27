from django import forms
from ..models import MedicoesCidade

class MedicoesCidadeForm(forms.ModelForm):
    class Meta:
        model = MedicoesCidade
        fields = ['cidade', 'sigla_pais']