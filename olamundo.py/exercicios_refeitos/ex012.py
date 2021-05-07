'''
ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
'''

preco_produto = float(input('Informe o preço do produto R$'))
novo_preco_produto = preco_produto - (preco_produto*5/100)
cores = {
    'limpa':'\033[m',
    'amarelo_bold':'\033[1;33m',
    'ciano_bold':'\033[1;36m'
}
print('O produto que custava {}R${:.2f}{}, na promoção com desconto de 5% vai custar {}R${:.2f}{}.'.format(cores['amarelo_bold'], preco_produto, cores['limpa'], cores['ciano_bold'], novo_preco_produto, cores['limpa']))
