'''
ex023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
      unidade: 4
      dezena: 3
      centena: 8
      milhar: 1
'''

from colorise import set_color, reset_color
cores = {
    'azul':'\033[1;34m',
    'limpa':'\033[m',
    'branco':'\033[0;97m'
}
set_color(fg='white')
num = int(input('Informe um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
reset_color()
print('\n{}Unidade:{} {}{}{}'.format(cores['branco'],cores['limpa'], cores['azul'], u, cores['limpa']))
print('{}Dezena:{} {}{}{}'.format(cores['branco'],cores['limpa'],cores['azul'],d, cores['limpa']))
print('{}Centena:{} {}{}{}'.format(cores['branco'], cores['limpa'], cores['azul'], c, cores['limpa']))
print('{}Milhar:{} {}{}{}'.format(cores['branco'], cores['limpa'], cores['azul'], m, cores['limpa']))
