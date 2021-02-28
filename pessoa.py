from salas import Salas
from espacos import Espacos

class Pessoa:
    def __init__(self):
        self.__dict_pessoas = {}
        self.__salas = Salas()
        self.__espacos = Espacos()

    def cadastro_pessoas(self):
        dict_pessoas = self.__dict_pessoas
        salas = self.__salas
        espacos = self.__espacos

        nome_pessoas = input('Nome: ')

        sobrenome_pessoas = input('Sobrenome: ')

        primeira_sala_pessoas = input(f'Primeira sala (entre {salas.consulta_salas_cadastro_pessoa()}): ')
        if primeira_sala_pessoas == None:
            print('Insira uma sala válida')
        elif primeira_sala_pessoas not in salas.consulta_salas_cadastro_pessoa():
            print('Insira uma sala válida')
        else:
            pass

        segunda_sala_pessoas = input(f'Segunda sala (entre {salas.consulta_salas_cadastro_pessoa()}): ')
        if segunda_sala_pessoas == None:
            print('Insira uma sala válida')
        elif segunda_sala_pessoas not in salas.consulta_salas_cadastro_pessoa():
            print('Insira uma sala válida')
        elif segunda_sala_pessoas == primeira_sala_pessoas:
            print('Insira uma sala que não tenha sido selecionada')
        else:
            pass

        espaço_pessoas = input(f'Espaço (entre {espacos.consulta_espaços_de_café_cadastro_pessoa()}): ')
        if espaço_pessoas == None:
            print('Insira um espaço válido')
        elif espaço_pessoas not in espacos.consulta_espaços_de_café_cadastro_pessoa():
            print('Insira um espaço válido')
        else:
            pass

        dict_pessoas[nome_pessoas] = sobrenome_pessoas, primeira_sala_pessoas, segunda_sala_pessoas, espaço_pessoas
        return dict_pessoas

    def consultar_pessoas(self):
        dict_pessoas = self.__dict_pessoas
        print('A seguir você irá ver uma relação de cada pessoa pela ordem de: Seu nome, sobrenome, primeira e segunda sala que realizará a prova, e o espaço de café designado.')
        print(dict_pessoas)
