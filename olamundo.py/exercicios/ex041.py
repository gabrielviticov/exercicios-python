'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

from datetime import date
ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_vigente = date.today().year
idade_atleta = ano_vigente - ano_nascimento
print('\nVocê atualmente tem ou terá {} anos até o final do ano vigente.'.format(idade_atleta))
if idade_atleta <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade_atleta <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade_atleta <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade_atleta <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
