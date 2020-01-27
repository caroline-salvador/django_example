import pyowm

from django.shortcuts import render, redirect
from .forms.medicoes_cidade_forms import MedicoesCidadeForm
from .services import medicoes_cidade_service, dados_climaticos_service
from .entidades.dados_climaticos import DadosClimaticos
from .entidades.medicoes_cidade import MedicoesCidade

def consultar_historico(request):
    form_medicoes_cidade = MedicoesCidadeForm()
    dados_climaticos = None

    if request.method == "POST":
        form_medicoes_cidade = MedicoesCidadeForm(request.POST)

        if form_medicoes_cidade.is_valid():
            cidade = form_medicoes_cidade.cleaned_data['cidade']
            sigla_pais = form_medicoes_cidade.cleaned_data['sigla_pais']

            dados = medicoes_cidade_service.buscar_cidade(cidade, sigla_pais)
            if dados:
                dados_climaticos = dados_climaticos_service.listar_dados_climaticos(dados.id)
                if not dados_climaticos:
                    return redirect('consultar_historico')

            return render(request, 'form_historico.html', {'dados_climaticos': dados_climaticos,
                                                           'medicoes_cidade': {'cidade': cidade,
                                                                               'sigla_pais': sigla_pais}})

    return render(request, 'form_consulta.html', {'form_medicoes_cidade': form_medicoes_cidade})

def consultar_clima(request):
    form_medicoes_cidade = MedicoesCidadeForm()
    if request.method == "POST":
        form_medicoes_cidade = MedicoesCidadeForm(request.POST)

        if form_medicoes_cidade.is_valid():
            cidade = form_medicoes_cidade.cleaned_data['cidade']
            sigla_pais = form_medicoes_cidade.cleaned_data['sigla_pais']

            obs = pesquisar_clima(cidade, sigla_pais)
            if obs:
                medicoes_cidade = medicoes_cidade_service.buscar_cidade(cidade=cidade, pais=sigla_pais)
                if not medicoes_cidade:
                    medicoes_cidade = medicoes_cidade_service.cadastrar_medicoes_cidade(MedicoesCidade(
                        cidade=cidade, sigla_pais=sigla_pais))

                dados_climaticos = cadastrar_dados_climaticos(obs, medicoes_cidade)
                return render(request, 'form_dados_climaticos.html', {'dados_climaticos': dados_climaticos,
                                                                      'medicoes_cidade': medicoes_cidade})

    return render(request, 'form_consulta.html', {'form_medicoes_cidade': form_medicoes_cidade})

def pesquisar_clima(cidade, pais):
    key = 'f2fff617bc81b445d7e40814cfbf301a'
    local = "{0}, {1}".format(cidade.lower(), pais.lower())

    try:
        owm = pyowm.OWM(key, language='pt')
        obs = owm.weather_at_place(local)
    except:
        return None

    return obs

def cadastrar_dados_climaticos(obs, medicoes_cidade):
    dados_clima = obs.get_weather()

    novo_dados_clima = DadosClimaticos(
        data_medicao=dados_clima.get_reference_time(timeformat='date').date().strftime("%Y-%m-%d"),
        hora_medicao=dados_clima.get_reference_time(timeformat='date').time().strftime("%H:%M:%S"),
        nascer_sol=dados_clima.get_sunrise_time('date').time().strftime("%H:%M:%S"),
        por_sol=dados_clima.get_sunset_time('date').time().strftime("%H:%M:%S"),
        temperatura_atual=dados_clima.get_temperature(unit='celsius')['temp'],
        temperatura_maxima=dados_clima.get_temperature(unit='celsius')['temp_max'],
        temperatura_minima=dados_clima.get_temperature(unit='celsius')['temp_min'],
        velocidade_vento=dados_clima.get_wind()['speed'],
        umidade_relativa_ar=dados_clima.get_humidity(),
        volume_chuva=dados_clima.get_rain().get('3h') and dados_clima.get_rain()['3h'] or 0,
        detalhes=dados_clima.get_detailed_status() and dados_clima.get_detailed_status() or "",
        medicoes_cidade=medicoes_cidade)

    dados_climaticos_service.cadastrar_dados_climaticos(novo_dados_clima)

    return novo_dados_clima
