'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

num = 0
d = 'S'
c = 0
m = 0
g = 0
menor = -1
maior = 1
soma_maior = 0
soma_menor = 0
while d not in 'Nn':
    c += 1
    num = int(input('Digite um número: '))
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    g += num
    d = str(input('Quer continuar? [S/N] '))
    m = (g)/c


print('Você digitou {} números e a média foi: {:.2f}'.format(c, m))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
