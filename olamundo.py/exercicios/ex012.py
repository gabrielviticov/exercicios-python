# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Informe o preço do produto R$'))
novo_preco = preco_produto - (preco_produto*5)/100
print('O produto que antes custava R${:.2f}\nHoje na promoção passa a custar R${:.2f}'.format(preco_produto, novo_preco))
