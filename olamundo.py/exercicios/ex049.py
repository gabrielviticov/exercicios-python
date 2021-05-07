'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

num = int(input('Digite um número inteiro para ver sua tabuada completa: '))
print('{:=^40}'.format(' TABUADA '))
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(num, c, num*c))
print('{:=^40}'.format(' TABUADA '))
