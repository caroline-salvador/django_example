class MedicoesCidade:
    def __init__(self, cidade, sigla_pais):
        self.__cidade = cidade
        self.__sigla_pais = sigla_pais

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def sigla_pais(self):
        return self.__sigla_pais

    @sigla_pais.setter
    def sigla_pais(self, sigla_pais):
        self.__sigla_pais = sigla_pais