'''
Estrutura de repetição (parte 3)
Interrompendo um laço de repetição: break

O comando break desvia a execução do looping para fora do looping, ou seja, ele interrompe um laço de excução.

ex:
n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma foi: {}'.format(s))
#f strings -
print(f'A soma vale: {s}')
print('Interrompido com sucesso!')

'''

