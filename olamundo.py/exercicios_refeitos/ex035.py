'''
ex035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

from colorise import set_color
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}
set_color(fg='green')
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    set_color(fg='green')
    print('\nOs segmentos acima {}FORMAM UM TRIÂNGULO!{}'.format(cor['white'], cor['limpa']))
else:
    set_color(fg='green')
    print('\nOs segmentos acima {}NÃO FORMAM UM TRIÂNGULO!{}'.format(cor['white'], cor['limpa']))