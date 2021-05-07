'''
Laços de repetição (parte 1)
Estrutura de repetição FOR:

[][][][][][] - Vamos supor que no primeiro bloco exista um personagem. Esse personagem gostaria de chegar no último bloco, pois lá existe uma maçã.
Para isso devemos dar os seguintes comandos:
personagem.siga(), personagem.siga(), personagem.siga(), personagem.siga(), personagem.siga(), personagem.pega().
Vamos ainda supor que exista uma mesma situação, só que, ainda mais longe. Percebemos que não é mais possível ficar utilizando comandos repetidos por várias vezes.

Vamos pegar um cenário maior: [I][][][][][][][][][][F] - (note: ponto I - Personagem e ponto F - Destino final).
Para que possamos utilizar um laço de repetição nesse caso: devo informar ao computador que o laço irá começar pelo número 1 e irá até o número 10 com um ÚNICO COMANDO "personagem.siga()".
Mais uma coisa: no ponto final "F" vamos supor que tenha uma maçã, o objetivo do personagem é, quando chegar no ponto "F", é ele parar de andar e pegar uma maçã. Com isso em mente, vamos codificar em Português para melhor compreensão:

laço <variavel> no intervalo (1, 10)
    siga
pegar

O comando "siga" irá se repetir até chegar no 10 e quando isso acabar, o comando "pega" será executado.

No Python usasse:

for <variavel> in range(1, 10):
    comando1
comando2

[I][] [][] [][] [][F]
resolução:
for <variavel> in range (0, 3):
    siga
    pula
siga
pegar

[I][] [*][] [][] [*][F] - * são colecionáveis
Veja que agora o cenário possuí colecionáveis e o personagem quer pega-los:
for <variavel> in range(0, 3):
    if colecionável:
        pega
    siga
    pula
siga
pega

ex:
for c in range(0, 10):
    print('OI')
print('FIM')

ex:
for c in range(0, 6):
    print('Olá')
    print('Gabriel')

ex:
for c in range(0, 10):
    print('Olá', end=' ')
    print('Gabriel')

ex:
for c in range(1, 11):
    print(c)

Para contar para trás:
for c in range(10, 0, -1):
    print(c)
print('FIM')

Para pular em dois em dois:
for c in range(0, 10, 2):
    print(c)
print('FIM')

ex:
n = int(input('Informe um número inteiro: '))
for c in range(0, n):
    print(c)
print('FIM')

n = int(input('Informe um número inteiro: '))
for c in range(0, n+1):
    print(c)
print('FIM')

ex:
i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

ex:
for c in range(0, 3):
    n = int(input('Informe um número: '))
print('FIM')

ex:
s = 0
for c in range(0, 3):
    n = int(input('Informe um número inteiro: '))
    s += n
print('O somatório vai ser {}'.format(s))
'''

