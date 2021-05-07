'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome_completo = str(input('Digite seu nome completo: ')).strip().title()
print('O seu nome tem Silva? {}'.format('Silva' in nome_completo))