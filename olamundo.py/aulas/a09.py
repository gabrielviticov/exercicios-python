'''
Estrutura de repetição:
Laço de repetição while:
    Como vimos anteriormente o exemplo de um algoritmo onde há uma estrutura de repetição for.
    A estrutura for precisa de uma coordenada de início e fim para ser utilizada. Mas existem casos em que não há como especificar o fim, pois não temos como saber onde esse algoritmo irá terminar. ex:
    [P][][][][][][][][][        ][?][B] - Ponto P e ponto B - Para a estrutura de repetição while (enquanto), eu posso especificar que: enquanto o ponto P não chegar no ponto B, ele ficará no loop até então chegar no ponto B. Perceba que nessa trilha há um ponto de interrogação, ela diz que não sabemos qual é o índice presente nessa trilha.

ex:
for c in range(1, 11):
    print(c)

c = 1                       ------> Eles são iguais!
while c < 11:
    print(c)
    c += 1

ex:
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('FIM')

ex:
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N]: '))
print('FIM')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Informe um número inteiro: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números PARES'.format(par))
print('Você digitou {} números ÍMPARES'.format(impar))
