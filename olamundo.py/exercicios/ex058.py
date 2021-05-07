'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
cont = 0
cpu = randint(0, 10)
print('O computador pensou em um número entre 0 e 10. Tente adivinhar!')
player = int(input('Informe um número: '))

while player != cpu:
    cpu = randint(0, 10)
    print('ERROU! Tente novamente. ')
    player = int(input('Informe um número: '))
    cont += 1
if player == cpu:
    cont += 1
    print('Acertou com {} tentativas. Parabéns!'.format(cont))
print('O computador pensou no número {}'.format(cpu))
