# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo pelo teclado: ')
print('O tipo primitivo desse valor é: {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanúmerico? {}'.format(a.isalnum()))
print('Está em maiúsulas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))
