'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

Fn = Fn - 1 + Fn - 2

3 + 2 = 5
5 + 3 = 8
8 + 5 = 13
13 + 8 = 21
21 + 13 = 34
34 + 21 = 55
55 + 34 = 89
'''

termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('{} -> {} ->'.format(t1, t2), end=' ')
while c <= termo:
    t3 = t1 + t2
    print('{} ->'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')