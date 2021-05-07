'''
ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘SILVA’ no nome.
'''

from colorise import set_color, reset_color
cores = {
    'limpa':'\033[m',
    'white_bold':'\033[1;97m'
}
set_color(fg='lightblue')
nome = str(input('Digite seu nome completo: ')).strip().title()
print('O seu nome tem Silva? ', end='')
reset_color()
print('{}{}{}'.format(cores['white_bold'], 'Silva' in nome, cores['limpa']))
