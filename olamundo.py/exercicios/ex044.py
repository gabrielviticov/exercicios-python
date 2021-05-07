'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

preco_produto = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')

print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
escolha = int(input('Qual é a opção escolhida? '))
if escolha == 1:
    novo_preco = preco_produto - (preco_produto * 10)/100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_produto, novo_preco))
elif escolha == 2:
    novo_preco = preco_produto - (preco_produto * 5)/100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_produto, novo_preco))
elif escolha == 3:
    parcela = int(input('Parcelado em 1 ou 2 vezes? '))
    novo_preco = preco_produto / parcela
    print('Sua compra de R${:.2f} vai custar custar {}x de R${:.2f}'.format(preco_produto, parcela, novo_preco))
elif escolha == 4:
    parcela_juros = int(input('Quantas parcelas? (obs: minímo 3): '))
    cal_juros = preco_produto + (preco_produto * 20) / 100
    novo_preco = cal_juros / parcela_juros
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela_juros, novo_preco))
    print('Sua compra de R${:.2f} vai custar R${:.2f} À PRAZO no final'.format(preco_produto, cal_juros))
else:
    print('Opção Inválida de pagamento. Tente novamente!')
