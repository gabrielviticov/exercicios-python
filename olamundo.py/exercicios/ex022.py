'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
primeiro_nome = nome.split()
print('Analisando seu nome...')
print('O seu nome em maiúsuclo é {}'.format(nome.upper()))
print('O seu nome em minúsculo é {}'.format(nome.lower()))
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))
