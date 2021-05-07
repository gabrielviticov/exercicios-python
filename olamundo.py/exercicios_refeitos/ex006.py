'''
ex006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''

num = int(input('Digite um número inteiro: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O número digitado foi: {}{}{}'.format('\033[1;34m', num, '\033[m'))
print('O seu dobro é: {}{}{}'.format('\033[1;31m', dobro, '\033[m'))
print('O seu triplo é: {}{}{}'.format('\033[1;35m', triplo, '\033[m'))
print('A sua raiz quadrada é: {}{:.3f}{}'.format('\033[1;36m', raiz, '\033[m'))
