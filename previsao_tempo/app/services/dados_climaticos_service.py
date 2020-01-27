from ..models import DadosClimaticos

def cadastrar_dados_climaticos(dados):
    dados.medicoes_cidade.dadosclimaticos_set.create(data_medicao=dados.data_medicao,
                                                     hora_medicao=dados.hora_medicao,
                                                     nascer_sol=dados.nascer_sol,
                                                     por_sol=dados.por_sol,
                                                     temperatura_atual=dados.temperatura_atual,
                                                     temperatura_minima=dados.temperatura_minima,
                                                     temperatura_maxima=dados.temperatura_maxima,
                                                     velocidade_vento=dados.velocidade_vento,
                                                     umidade_relativa_ar=dados.umidade_relativa_ar,
                                                     volume_chuva=dados.volume_chuva,
                                                     detalhes=dados.detalhes)
    return

def listar_dados_climaticos(id):
    dados_climaticos = DadosClimaticos.objects.filter(medicoes_cidade=id)
    return dados_climaticos
