'''
ex026: Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra ‘A’
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
'''


cores = {
    'limpa':'\033[m',
    'white_bold':'\033[1;97m',
    'green':'\033[1;32m'
}
a = str(input('Digite uma frase: ')).strip().upper()
print('\n{}A letra "A" apareceu{} {}{} vezes {}{}na frase{}'.format(cores['green'],cores['limpa'],cores['white_bold'],a.count('A'), cores['limpa'], cores['green'], cores['limpa']))
print('{}A primeira letra "A" apareceu na{} {}posição {}{}'.format(cores['green'],cores['limpa'],cores['white_bold'],a.find('A') + 1, cores['limpa']))
print('{}A última letra "A" apareceu na{} {}posição {}{}'.format(cores['green'], cores['limpa'], cores['white_bold'],a.rfind('A') + 1, cores['limpa']))