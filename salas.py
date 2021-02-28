class Salas:
    def __init__(self):
        self.__dict_salas = {}

    def cadastro_salas(self):
        dict_salas = self.__dict_salas

        nome_salas = input('Nome da sala: ')

        lotação_salas = input('Lotação da sala: ')

        dict_salas[nome_salas] = lotação_salas
        return dict_salas

    def consulta_salas(self):
        dict_salas = self.__dict_salas
        print('A seguir você irá ver uma relação de cada sala pela ordem de: Seu nome e lotação')
        print(dict_salas)

    def consulta_salas_cadastro_pessoa(self):
        dict_salas = self.__dict_salas
        return dict_salas