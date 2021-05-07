'''
ex022: Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo(sem considerar espaços)
Quantas letras tem o primeiro nome.
'''

from colorise import set_color, reset_color
cores = {
    'limpa':'\033[m',
    'lightgreen':'\033[1;92m',
    'white_bold':'\033[1;97m'
}
set_color(fg='white'); nome_completo = str(input('Informe o seu nome completo: ').format()).strip()
reset_color()
print('{}O seu nome em maiúsculo é: {}{}{}{}'.format(cores['lightgreen'],cores['limpa'],cores['white_bold'],nome_completo.upper(), cores['limpa']))
print('{}O seu nome em minúsculo é:{} {}{}{}'.format(cores['lightgreen'],cores['limpa'],cores['white_bold'],nome_completo.lower(), cores['limpa']))
print('{}O seu nome tem:{} {}{} letras{}'.format(cores['lightgreen'],cores['limpa'],cores['white_bold'],len(nome_completo) - nome_completo.count(' '), cores['limpa']))
primeiro_nome = nome_completo.split()
print('{}O seu primeiro nome{} {}{} {}tem{} {}{} letras{}'.format(cores['lightgreen'],cores['limpa'],cores['white_bold'],primeiro_nome[0],cores['lightgreen'],cores['limpa'], cores['white_bold'],len(primeiro_nome[0]), cores['limpa']))
