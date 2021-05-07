'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''


num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print('Fatorial {}! ='.format(num), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

'''from math import factorial
num = int(input('Digite um número: '))
i = (num - num)
cont = num
f = factorial(num)
print('{}! ='.format(num), end=' ')
for c in range(i, num):
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=', end=' ')
    cont -= 1
print('{}'.format(f))'''