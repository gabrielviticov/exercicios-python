'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
items = ('Pedra', 'Papel', 'Tesoura', 'Inválido')
cpu = randint(0, 2)
print('''
Suas opções:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
player = int(input('Qual é a sua jogada? (obs: escolha um número): '))
print('\nO jogador jogou {}'.format(items[player]))
print('O computador jogou {}'.format(items[cpu]))
if cpu == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCEU')
    elif player == 2:
        print('COMPUTADOR VENDEU')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 1:
    if player == 0:
        print('COMPUTADOR VENDEU')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENDEU')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 2:
    if player == 0:
        print('JOGADOR VENDEU')
    elif player == 1:
        print('COMPUTADOR VENDEU')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
