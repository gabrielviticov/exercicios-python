'''
Utilizando módulos em Python

    import <nome_da_biblioteca>; importará todos os módulos disponiveis da biblioteca
    from <nome_da_biblioteca> import <nome_do(s)_módulo(s)>; importará apenas alguns módulos especificados

    biblioteca built in: math
    a biblioteca math possui alguns módulos:
    ceil (arredonda para cima)
    floor (arredonda para baixo)
    trunc (trunca um número, eliminando os pontos flutuantes)
    pow (calculo de exponenciação)
    sqrt (calculo de raíz quadrada)
    factorial (calculo de fatorial)

from math import sqrt, pow
num = int(input('Digite um número inteiro: '))
raiz = sqrt(num)
pot = pow(num, 2)
print('A raíz quadrada de {} equivale à {}'.format(num, raiz))
print('O número {} elevado ao quadrado equivale à {}'.format(num, pot))

    biblioteca built in: random
    random (gera um número real aleatório entre 0 e 1)
    randint (gera um número inteiro aleatório. É necessário especificar o inicio e o fim) ex: randint(1, 10)

import random

cpu1 = random.random()
cpu2 = random.randint(1, 10)
print(cpu1)
print(cpu2)




import emoji
print(emoji.emojize('Olá, mundo! :earth_americas:', use_aliases=True))

'''

