# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#(0 °C × 9/5) + 32 = 32 °F

celsius = float(input('Informe a temperatura atual ºC: '))
fahrenheit = (celsius * 9/5) + 32
print('A temperatura de {:.1f}ºC\nEquivale a {:.1f}ºF em Fahrenheit'.format(celsius, fahrenheit))
