# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_funcionario = float(input('Informe o salário do funcionário R$'))
aumento_salario_funcionario = salario_funcionario + (salario_funcionario*15)/100
print('O funcionário que antes recebia um salário de R${:.2f}\nPassa a receber R${:.2f} por conta do aumento do salário em 15%'.format(salario_funcionario, aumento_salario_funcionario))
