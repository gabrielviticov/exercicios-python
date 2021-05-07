'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

num = cont = p = 0
num = int(input('Digite um número: '))
p = num
while True:
    print(f'{num} x {cont} = {num*cont:2}')
    if num < 0:
        break
    cont += 1
    if cont == 10:
        cont = 0
        num = int(input('Quer ver a tabuada de qual valor? '))
        while cont <= 10:
            print(f'{num} x {cont} = {num*cont:2}')
            cont += 1