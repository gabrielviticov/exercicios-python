'''
ex024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘SANTO’
'''

from colorise import set_color, reset_color

cores = {
    'limpa': '\033[m',
    'white': '\033[1;97m',
}
set_color(fg='cyan')
nome_cidade = str(input('Informe o nome de uma cidade: ')).strip().title()
separador = nome_cidade.split()
print('O nome da cidade começa com Santo? ', end='')
reset_color()
print('{}{}{}'.format(cores['white'], separador[0] == 'Santo', cores['limpa']))
