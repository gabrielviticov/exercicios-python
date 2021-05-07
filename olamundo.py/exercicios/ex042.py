'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima FORMAM UM TRIÂNGULO', end=' ')
    if r1 == r2 and r1 == r3: #pode se fazer: r1 == r2 == r3; r1 == r2 and r1 == r3; os três casos funcionam
        print('(EQUILÁTERO!)')
    elif r1 == r2 or r1 == r3:
        print('(ISÓSCELES!)')
    elif r1 != r2 and r1 != r3:
        print('(ESCALENO!)')
else:
    print('\nOs segmentos acima NÃO FORMAM UM TRIÂNGULO!')