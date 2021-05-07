'''
Faça um programa em PYTHON que leia o valor atual do salário de um funcionário. Informe o valor de seu salário REAJUSTADO, de acordo com os percentuais indicados a seguir:

50% para aqueles que recebem até R$ 2.000,00.
20% para aqueles que recebem mais de R$ 2.000,00 e menos de R$ 5.000,00.
10% para os demais.
'''

salario_funcionario = float(input('Informe o salário do funcionário R$'))
if salario_funcionario <= 2000:
    reajuste = salario_funcionario + (salario_funcionario * 50)/100
elif salario_funcionario > 2000 and salario_funcionario < 5000:
    reajuste = salario_funcionario + (salario_funcionario * 20)/100
else:
    reajuste = salario_funcionario + (salario_funcionario * 10)/100
print('\nO funcionário que antes ganhava um salário de R${:.2f}'.format(salario_funcionario))
print('Passa a ganhar hoje R${:.2f} por conta do reajuste salarial.'.format(reajuste))
