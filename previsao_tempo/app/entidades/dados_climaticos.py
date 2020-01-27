class DadosClimaticos:
    def __init__(self, data_medicao, hora_medicao, nascer_sol, por_sol, temperatura_atual, temperatura_minima, temperatura_maxima,
                 velocidade_vento, umidade_relativa_ar, volume_chuva, detalhes, medicoes_cidade):

        self.__data_medicao = data_medicao
        self.__hora_medicao = hora_medicao
        self.__nascer_sol = nascer_sol
        self.__por_sol = por_sol
        self.__temperatura_atual = temperatura_atual
        self.__temperatura_minima = temperatura_minima
        self.__temperatura_maxima = temperatura_maxima
        self.__velocidade_vento = velocidade_vento
        self.__umidade_relativa_ar = umidade_relativa_ar
        self.__volume_chuva = volume_chuva
        self.__detalhes = detalhes
        self.__medicoes_cidade = medicoes_cidade

    @property
    def data_medicao(self):
        return self.__data_medicao

    @data_medicao.setter
    def data_medicao(self, data_medicao):
        self.__data_medicao = data_medicao

    # ----------
    @property
    def hora_medicao(self):
        return self.__hora_medicao

    @hora_medicao.setter
    def hora_medicao(self, hora_medicao):
        self.__hora_medicao = hora_medicao

    # ----------
    @property
    def nascer_sol(self):
        return self.__nascer_sol

    @nascer_sol.setter
    def nascer_sol(self, nascer_sol):
        self.__nascer_sol = nascer_sol

    # ----------
    @property
    def por_sol(self):
        return self.__por_sol

    @por_sol.setter
    def por_sol(self, por_sol):
        self.__por_sol = por_sol

    # ----------
    @property
    def temperatura_atual(self):
        return self.__temperatura_atual

    @temperatura_atual.setter
    def temperatura_atual(self, temperatura_atual):
        self.__temperatura_atual = temperatura_atual

    # ----------
    @property
    def temperatura_minima(self):
        return self.__temperatura_minima

    @temperatura_minima.setter
    def temperatura_minima(self, temperatura_minima):
        self.__temperatura_minima = temperatura_minima

    # ----------
    @property
    def temperatura_maxima(self):
        return self.__temperatura_maxima

    @temperatura_maxima.setter
    def temperatura_maxima(self, temperatura_maxima):
        self.__temperatura_maxima = temperatura_maxima

    # ----------
    @property
    def velocidade_vento(self):
        return self.__velocidade_vento

    @velocidade_vento.setter
    def velocidade_vento(self, velocidade_vento):
        self.__velocidade_vento = velocidade_vento

    # ----------
    @property
    def umidade_relativa_ar(self):
        return self.__umidade_relativa_ar

    @umidade_relativa_ar.setter
    def umidade_relativa_ar(self, umidade_relativa_ar):
        self.__umidade_relativa_ar = umidade_relativa_ar

    # ----------
    @property
    def volume_chuva(self):
        return self.__volume_chuva

    @volume_chuva.setter
    def volume_chuva(self, volume_chuva):
        self.__volume_chuva = volume_chuva

    # ----------
    @property
    def detalhes(self):
        return self.__detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        self.__detalhes = detalhes

    # ----------
    @property
    def medicoes_cidade(self):
        return self.__medicoes_cidade

    @medicoes_cidade.setter
    def medicoes_cidade(self, medicoes_cidade):
        self.__medicoes_cidade = medicoes_cidade
