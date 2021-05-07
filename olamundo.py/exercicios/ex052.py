'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# exercicio resolvido com ajuda do professor
'''

num = int(input('Informe um número inteiro: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('{}{}{}'.format('\033[1;34m', c, '\033[m'), end=' ')
        total += 1
    else:
        print('{}'.format(c), end=' ')
print('\nO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('ELE É UM NÚMERO PRIMO!')
else:
    print('ELE NÃO É UM NÚMERO PRIMO')
