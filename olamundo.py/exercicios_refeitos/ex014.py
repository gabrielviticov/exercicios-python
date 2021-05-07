'''
ex014: Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF
fórmula: (0 °C × 9/5) + 32 = 32 °F
'''

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celsius * 9 / 5) + 32
cores = {
    'limpa':'\033[m',
    'verde_bold':'\033[1;32m',
    'vermelho_bold':'\033[1;31m'
}
print('A temperatura de {}{}ºC{} equivale à {}{}ºF{} em Fahrenheit'.format(cores['vermelho_bold'], celsius, cores['limpa'], cores['verde_bold'], fahrenheit, cores['limpa']))
