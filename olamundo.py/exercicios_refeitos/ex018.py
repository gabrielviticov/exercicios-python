'''
ex018: Faça um programa que leia um ângulo qualquer a mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
import colorise

colorise.set_color(fg='green'); angulo = int(input('Informe o ângulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
colorise.set_color(fg='cyan'); print('Para um ângulo de: ', end='')
colorise.set_color(fg='white')
print('{}ºC'.format(angulo))
colorise.set_color(fg='cyan')
print('Temos o SENO de: ', end='')
colorise.set_color(fg='white')
print('{:.2f}'.format(seno))
colorise.set_color(fg='cyan')
print('Temos o COSSENO de ', end='')
colorise.set_color(fg='white')
print('{:.2f}'.format(cosseno))
colorise.set_color(fg='blue')
print('Temos a TANGENTE de ', end='')
colorise.set_color(fg='white')
print('{:.2f}'.format(tangente))
