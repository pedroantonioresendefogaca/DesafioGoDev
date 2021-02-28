from pessoa import Pessoa
from espacos import Espacos
from salas import Salas

pessoa = Pessoa()
espacos = Espacos()
salas = Salas()

while True:
    try:
        interface = int(input('!!!DESAFIO GODEV!!!\nInsira a operação que gostaria de realizar\n1 - Cadastro de pessoas\n2 - Consulta de pessoas\n3 - Cadastro de salas\n4 - Consulta de salas\n5 - Cadastro de espaços de café\n6 - Consulta de espaços de café\n7 - Sair\nInsira a operação desejada: '))
        if interface == 1:
            pessoa.cadastro_pessoas()
        elif interface == 2:
            pessoa.consultar_pessoas()
        elif interface == 3:
            salas.cadastro_salas()
        elif interface == 4:
            salas.consulta_salas()
        elif interface == 5:
            espacos.cadastro_espaços_de_café()
        elif interface == 6:
            espacos.consulta_espaços_de_café()
        elif interface == 7:
            print('Obrigado por utilizar o sistema!')
            break
    except ValueError:
        print('Insira uma operação válida')
