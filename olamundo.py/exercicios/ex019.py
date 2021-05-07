# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = str(input('Informe o nome do primeiro(a) aluno(a): '))
a2 = str(input('Informe o nome do segundo(a) aluno(a): '))
a3 = str(input('Informe o nome do terceiro(a) aluno(a): '))
a4 = str(input('Informe o nome do quarto(a) aluno(a): '))
lista_alunos = [a1, a2, a3, a4]
escolhido = random.choice(lista_alunos)
print('O(a) aluno(a) escolhido foi: {}'.format(escolhido))
