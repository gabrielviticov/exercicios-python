'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))

if n1 < n2 and n1 < n3:
    print('O menor número digitado foi: {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número digitado foi: {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número digitado foi: {}'.format(n3))

if n1 > n2 and n1 > n3:
    print('O maior número digitado foi: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número digitado foi: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número digitado foi: {}'.format(n3))