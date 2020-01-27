from ..models import MedicoesCidade

def buscar_cidade(cidade, pais):
    try:
        dados_cidade = MedicoesCidade.objects.get(cidade=cidade, sigla_pais=pais)
    except:
        dados_cidade = None
        pass

    return dados_cidade


def cadastrar_medicoes_cidade(dados):
    return MedicoesCidade.objects.create(cidade=dados.cidade, sigla_pais=dados.sigla_pais)
