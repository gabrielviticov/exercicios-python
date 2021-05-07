'''
ex003: Crie um programa que leia dois números e mostre a soma entre eles
'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
soma = num1 + num2
print('A soma entre {}{} + {}{} = {}{}{}'.format('\033[1;36m', num1, num2, '\033[m', '\033[1;32m', soma, '\033[m'))
