'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

#forma de string - forma 1
#num = int(input('Informe um número entre 1 à 9999: '))
#n = str(num)
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
#como não estamos utilizando estrutura de repetição, esse programa é um grande erro, basta colocar um número inferior à 4 casas decimais

#forma matemática - forma 2

num = int(input('Informe um número entre 1 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
