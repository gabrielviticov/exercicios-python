'''
ex033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

from colorise import set_color, reset_color
set_color(fg='green')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}

set_color(fg='green')
if n1 > n2 and n1 > n3:
    set_color(fg='green')
    print('\nO maior número é: {}{}{}'.format(cor['white'], n1, cor['limpa']))
if n2 > n1 and n2 > n3:
    set_color(fg='green')
    print('\nO maior número é: {}{}{}'.format(cor['white'], n2, cor['limpa']))
if n3 > n1 and n3 > n2:
    set_color(fg='green')
    print('\nO maior número é: {}{}{}'.format(cor['white'], n3, cor['limpa']))
if n1 < n2 and n1 < n3:
    set_color(fg='green')
    print('O menor número é: {}{}{}'.format(cor['white'], n1, cor['limpa']))
if n2 < n1 and n2 < n3:
    set_color(fg='green')
    print('O menor número é: {}{}{}'.format(cor['white'], n2, cor['limpa']))
if n3 < n1 and n3 < n2:
    set_color(fg='green')
    print('O menor número é: {}{}{}'.format(cor['white'], n3, cor['limpa']))