'''
ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
   primeiro = Ana
   último = Souza
'''

from colorise import set_color, reset_color

cor = {
    'limpa': '\033[m',
    'white': '\033[1;97m'
}
set_color(fg='green')
nome_completo = str(input('Informe o seu nome completo: ')).strip().title()
nome_lista = nome_completo.split()
print('\nSeu primeiro nome é: ', end='')
reset_color()
print('{}{}{}'.format(cor['white'], nome_lista[0], cor['limpa']))
set_color(fg='green')
print('O seu último nome é: ', end='')
reset_color()
print('{}{}{}'.format(cor['white'], nome_lista[len(nome_lista) - 1], cor['limpa']))
