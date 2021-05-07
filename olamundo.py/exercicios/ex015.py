# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe quantos KMs percorridos: '))
car = int(input('Informe quantos dias o carro foi alugado: '))
pagar = (car*60) + (km*0.15)
print('O valor a se pagar é de R${:.2f}'.format(pagar))
