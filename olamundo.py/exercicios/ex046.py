'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

print('{:=^40}'.format(' CONTAGEM REGRESSIVA '))
from time import sleep
from emoji import emojize
for c in range(10, -1, -1): #-1 diz que será de cima para baixo: 10, 9, 8, 7...
    sleep(1)
    print('{:2}'.format(c))
print(emojize('BOOM! BOOM! POOW! :fireworks: :sparkles:',use_aliases='True'))
print('{:=^40}'.format(' FIM DA CONTAGEM REGRESSIVA '))