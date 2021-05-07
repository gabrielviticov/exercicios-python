'''
ex030: Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''

from colorise import set_color, reset_color
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}
set_color(fg='green')
num = int(input('Informe um número inteiro: '))
if num % 2 == 0:
    print('{}\nPAR!{}'.format(cor['white'], cor['limpa']))
else:
    print('{}\nÍMPAR!{}'.format(cor['white'], cor['limpa']))
