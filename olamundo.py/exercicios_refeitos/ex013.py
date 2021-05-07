'''
ex013: Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento
'''

salario_funcionario = float(input('Informe o salário do funcionário R$'))
novo_salario_funcionario = salario_funcionario + (salario_funcionario * 15 / 100)
cores = {
    'limpa':'\033[m',
    'amarelo_bold':'\033[1;33m',
    'ciano_bold':'\033[1;36m'
}
print('O funcionário que antes ganhava {}R${:.2f}{}, com um aumento de 15%, passa a receber {}R${:.2f}{}.'.format(cores['amarelo_bold'], salario_funcionario, cores['limpa'], cores['ciano_bold'], novo_salario_funcionario, cores['limpa']))
