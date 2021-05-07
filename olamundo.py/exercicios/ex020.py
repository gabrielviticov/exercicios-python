# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1 = str(input('Informe o nome do(a) primeiro(a) aluno(a): '))
a2 = str(input('Informe o nome do(a) segundo(a) aluno(a): '))
a3 = str(input('Informe o nome do(a) terceiro(a) aluno(a): '))
a4 = str(input('Informe o nome do(a) quarto(a) aluno(a): '))
lista_alunos = [a1, a2, a3, a4]
ordem = random.shuffle(lista_alunos)
print('A ordem de apresentação será: {}'.format(lista_alunos))
