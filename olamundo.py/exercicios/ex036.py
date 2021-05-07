'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Informe o valor da casa R$'))
salario_comprador = float(input('Informe o seu salário R$'))
anos_financiamento = int(input('Quantos anos você pretende pagar?: '))
mes_financiamento = anos_financiamento * 12
cal_prestacao = valor_casa / mes_financiamento
salario30 = (salario_comprador * 30)/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} mensais'.format(valor_casa, anos_financiamento, cal_prestacao))
if cal_prestacao > salario30:
    print('Emprestimo negado')
elif cal_prestacao <= salario30:
    print('Emprestimo concedido')
