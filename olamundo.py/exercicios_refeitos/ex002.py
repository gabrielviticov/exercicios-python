'''
ex002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas
'''

nome = str(input('Como você gostaria de ser chamado: '))
print('Olá {}{}{}, prazer em te conhecer!'.format('\033[1;31m', nome, '\033[m'))
