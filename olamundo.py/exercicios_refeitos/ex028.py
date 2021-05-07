'''
ex028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from colorise import set_color, reset_color
from time import sleep
set_color(fg='green')
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}
print('VOU PENSAR EM UM NÚMERO INTEIRO ENTRE 0 E 5. TENTE ADIVINHAR!')
sleep(3)
player = int(input('Em que número você acha que o computador pensou? '))
cpu = randint(0, 5)
sleep(3)
reset_color()
if player == cpu:
    print('\n{}ACERTOU!{}'.format(cor['white'], cor['limpa']))
else:
    print('{}ERROU!{}'.format(cor['white'], cor['limpa']))
sleep(2)
set_color(fg='white')
print('O computador pensou no número: {}'.format(cpu))