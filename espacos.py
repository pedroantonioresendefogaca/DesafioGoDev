class Espacos:
    def __init__(self):
        self.__dict_espaços_de_café = {}

    def cadastro_espaços_de_café(self):
        dict_espaços_de_café = self.__dict_espaços_de_café

        nome_espaços = input('Nome do espaço: ')

        lotação_espaços = input('Lotação do espaço: ')

        dict_espaços_de_café[nome_espaços] = lotação_espaços
        return dict_espaços_de_café

    def consulta_espaços_de_café(self):
        dict_espaços_de_café = self.__dict_espaços_de_café
        print('A seguir você irá ver uma relação de cada espaço de café pela ordem de: Seu nome e lotação')
        print(dict_espaços_de_café)

    def consulta_espaços_de_café_cadastro_pessoa(self):
        dict_espaços_de_café = self.__dict_espaços_de_café
        return dict_espaços_de_café