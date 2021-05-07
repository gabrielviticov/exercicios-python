'''
ex016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex: Digite um número: 6.127
      O número 6.127 tem a parte Inteira 6.
'''

import colorise
colorise.color_names()
colorise.set_color(fg='cyan'); num_real = float(input('Digite um número real: '))
colorise.set_color(fg='yellow'); print('O número digitado foi: {}\nA sua porção inteira é: {}'.format(num_real, int(num_real)))
