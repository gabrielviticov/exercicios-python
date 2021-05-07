'''
ex009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
'''

num = int(input('Digite um número para ver sua tabuada: '))
cores = {
    'limpa':'\033[m',
    'vermelho_bold':'\033[1;31m',
    'ciano_bold':'\033[1;36m',
    'branco_bold':'\033[1;97m'
}
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 1, cores['limpa'], cores['branco_bold'], num*1, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 2, cores['limpa'], cores['branco_bold'], num*2, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 3, cores['limpa'], cores['branco_bold'], num*3, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 4, cores['limpa'], cores['branco_bold'], num*4, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 5, cores['limpa'], cores['branco_bold'], num*5, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 6, cores['limpa'], cores['branco_bold'], num*6, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 7, cores['limpa'], cores['branco_bold'], num*7, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 8, cores['limpa'], cores['branco_bold'], num*8, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 9, cores['limpa'], cores['branco_bold'], num*9, cores['limpa']))
print('{}{}{} x {}{}{} = {}{:2}{}'.format(cores['vermelho_bold'], num, cores['limpa'], cores['ciano_bold'], 10, cores['limpa'], cores['branco_bold'], num*10, cores['limpa']))