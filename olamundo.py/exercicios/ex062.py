'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
t = p1
m = 10
tot = 0
while m != 0:
    tot = tot + m
    while c <= tot:
        print('{} ->'.format(t), end=' ')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantidade de termos: '))
print('Progressão finalizada com {} termos mostrados'.format(tot))
