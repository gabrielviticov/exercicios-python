'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. A maioridade é 18.
'''

from datetime import date
ano_atual = date.today().year
cont_maioridade = 0
cont = 0
for c in range (1, 8):
    ano_nascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        cont_maioridade += 1
    else:
        cont += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(cont_maioridade))
print('E também tivemos {} pessoas menores de idade'.format(cont))
