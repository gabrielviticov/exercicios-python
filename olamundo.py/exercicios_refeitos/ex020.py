'''
ex:020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import colorise
import random

colorise.set_color(fg='green')
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será: ', end='')
colorise.set_color(fg='white')
print('{}.'.format(lista))