'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('\nO aluno obteve a média: {:.1f}'.format(media))
if media >= 7.0:
    print('O aluno foi APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno foi REPROVADO!')
