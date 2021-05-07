'''
ex007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
'''

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Caro aluno, você obteve a média: {}{}{}'.format('\033[1;94m', media, '\033[m'))
