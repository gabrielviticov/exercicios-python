'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p1
c = 1
while c <= 10:
    print('{} ->'.format(t), end=' ')
    t += r
    c += 1
print('FIM')
