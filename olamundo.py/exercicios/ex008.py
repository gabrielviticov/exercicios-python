# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Valor em metros: '))
ce = metros * 100
mi = metros * 1000
print('O valor digitado é: {} metros\nEquivale à {} centímetros\nE {} milímetros'.format(metros, ce, mi))
