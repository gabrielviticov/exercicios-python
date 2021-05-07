'''
ex019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
'''

import colorise
import random

colorise.set_color(fg='lightgreen')
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)
colorise.set_color(fg='lightyellow')
print('O aluno escolhido foi: ', end='')
colorise.set_color(fg='white')
print('{}.'.format(escolhido))
