# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = int(input('Informe o ângulo desejado: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {}º tem o SENO de {:.2f}'.format(an, seno))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(an, tangente))
