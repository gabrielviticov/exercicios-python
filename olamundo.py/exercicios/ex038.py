'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe mais número inteiro: '))
if n1 > n2:
    print('\nO primeiro valor é MAIOR')
elif n1 < n2:
    print('\nO segundo valor é MAIOR')
elif n1 == n2:
    print('\nNão existe valor maior, os dois são IGUAIS')
