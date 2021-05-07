'''
ex004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
'''

a = input('Digite algo pelo teclado: ')
print('O seu tipo primitivo é: {}{}{}'.format('\033[1;31m', type(a), '\033[m'))
print('Só tem espaços? {}{}{}'.format('\033[1;32m', a.isspace(), '\033[m'))
print('É um número? {}{}{}'.format('\033[1;33m', a.isnumeric(), '\033[m'))
print('É alfabético? {}{}{}'.format('\033[1;34m', a.isalpha(), '\033[m'))
print('É alfanúmerico? {}{}{}'.format('\033[1;35m', a.isalnum(), '\033[m'))
print('Está em maiúsculas? {}{}{}'.format('\033[1;36m', a.isupper(), '\033[m'))
print('Está em minúsculas? {}{}{}'.format('\033[1;37m', a.islower(), '\033[m'))
print('Está capitalizada? {}{}{}'.format('\033[1;38m', a.istitle(), '\033[m'))
