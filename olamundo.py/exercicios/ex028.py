'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
cpu = randint(0, 5)
print('O computador irá escolher um número entre 0 e 5. TENTE ADIVINHAR!')
player = int(input('Digite o número escolhido: '))
if player == cpu:
    print('Você acertou!')
else:
    print('Você errou!')
print('O computador escolheu o número {}'.format(cpu))
