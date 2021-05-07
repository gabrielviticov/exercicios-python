'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salario_funcionario = float(input('Digite o salário do funcionário R$'))
if salario_funcionario > 1250.00:
    novo_salario = salario_funcionario + (salario_funcionario * 10 / 100)
else:
    novo_salario = salario_funcionario + (salario_funcionario * 15 / 100)
print('O seu novo salário será de R${:.2f}'.format(novo_salario))
