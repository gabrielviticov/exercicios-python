'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

nome_cidade = str(input('Digite o nome de uma cidade: ')).strip()
primeiro_nome = nome_cidade.split()
print('{}'.format('Santo' in primeiro_nome[0].capitalize()))
