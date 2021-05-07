'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# - pontos que precisam seres melhorados - não foi capaz de implementar sem ajuda
'''

from datetime import date
ano_atual = date.today().year #sinconizar a o ano da máquina. Isso será muito importante no programa
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade_jovem = ano_atual - ano_nascimento
if idade_jovem == 18:
    print('Você precisa se alistar agora, pois você tem ou terá {} anos até o fim desse ano vigente!'.format(idade_jovem))
elif idade_jovem < 18:
    saldo = 18 - idade_jovem #
    ano_alistamento = ano_atual + saldo #
    print('Você ainda é novo para se alistar. Você deverá se alista daqui a {} anos'.format(saldo))
    print('Você irá se alistar no ano de {}'.format(ano_alistamento))
elif idade_jovem > 18:
    saldo = idade_jovem - 18 #
    ano_alistamento = ano_atual - saldo #
    print('Já passou da hora de se alistar. Você deveria ter se alistado há {} anos atrás.'.format(saldo))
    print('Você deveria ter se alistado no ano de {}'.format(ano_alistamento))