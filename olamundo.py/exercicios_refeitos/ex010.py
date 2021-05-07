'''
ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
Considere US$ 1,00 = R$ 3,27
'''

carteira = float(input('Quantos reais você tem em sua carteira? R$'))
dollar = carteira / 3.27
cores = {
    'limpa':'\033[m',
    'verde_bold':'\033[1;32m',
    'ciano_bold':'\033[1;36m'
}
print('Você possui {}R${:.2f}{}'.format(cores['verde_bold'], carteira, cores['limpa']))
print('Logo você pode comprar até {}${:.2f}{} dólar(es) americano(s)'.format(cores['ciano_bold'], dollar, cores['limpa']))
