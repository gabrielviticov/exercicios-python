'''
ex034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

from colorise import set_color
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}
set_color(fg='green')
salario_funcionario = float(input('Informe o salário do funcionário R$'))
if salario_funcionario > 1250.00:
    aumento = salario_funcionario + (salario_funcionario * 10)/100
else:
    aumento = salario_funcionario + (salario_funcionario * 15)/100
print('\nO funcionário que antes ganhava {}R${:.2f}{}'.format(cor['white'],salario_funcionario,cor['limpa'], ))
set_color(fg='green')
print('Passa a receber {}R${:.2f}{}'.format(cor['white'], aumento, cor['limpa']))
