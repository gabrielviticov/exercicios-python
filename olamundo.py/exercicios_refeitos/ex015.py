'''
ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
'''

km_percorridos = float(input('Informe a quantidade de KM percorridos: '))
dias_alugados = int(input('Informe a quantidade de dias que o carro foi alugado: '))
total_pagar = (dias_alugados * 60) + (km_percorridos * 0.15)
cores = {
    'limpa':'\033[m',
    'azul_bold':'\033[1;34m'
}
print('O total a se pagar é de {}R${:.2f}{}'.format(cores['azul_bold'], total_pagar, cores['limpa']))
