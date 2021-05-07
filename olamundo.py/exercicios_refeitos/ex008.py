'''
ex008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''

metros = float(input('Informe o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('O valor digitado foi: {}{}{}{}'.format('\033[0;93m', metros, 'm', '\033[m'))
print('Isso equivale à {}{}{} centímetros'.format('\033[0;93m', centimetros, '\033[m'))
print('E também equivale à {}{}{} milímetros'.format('\033[0;93m', milimetros, '\033[m'))
