'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA P.A'))
print('='*30)


a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1 + (10-1) * r

for c in range(a1, an+r, r): #a1 = Início, n = Total, r = Pular
    print('{:.^}'.format(c), end=' ➝ ')
print('ACABOU')