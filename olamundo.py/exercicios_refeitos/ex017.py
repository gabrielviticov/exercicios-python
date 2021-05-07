'''
ex:017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule o mostre o comprimento da hipotenusa.
'''

import math
import colorise

print('==='*20)
colorise.set_color(fg='lightgreen'); co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa irá medir: ', end='')
colorise.set_color(fg='lightred'); print('{:.2f}'.format(hi))
colorise.reset_color(); print('==='*20)