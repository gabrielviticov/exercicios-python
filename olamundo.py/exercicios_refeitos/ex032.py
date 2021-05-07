'''
ex032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''

from datetime import date
from colorise import set_color, reset_color
cor = {
    'limpa':'\033[m',
    'white_bold':'\033[1;97m'
}
set_color(fg='green')
ano = int(input('Informe o ano que deseja analisar. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    set_color(fg='green')
    print('\nO ano informado é {}BISSEXTO!{}'.format(cor['white_bold'], cor['limpa']))
else:
    set_color(fg='green')
    print('\nO ano informado {}NÃO É BISSEXTO!{}'.format(cor['white_bold'], cor['limpa']))
set_color(fg='green')
print('O ano informado foi {}{}{}'.format(cor['white_bold'], ano, cor['limpa']))