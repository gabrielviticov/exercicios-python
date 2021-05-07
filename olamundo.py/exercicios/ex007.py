# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Infome a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2)/2
print('Caro aluno, você obteve uma média: {:.1f}'.format(media))
