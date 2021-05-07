##crie um script Pyhton que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

print('Informe sua data de nascimento no campo abaixo, informando o dia, o mês e o ano')
dia = input('Diga-me, que dia você nasceu: ')
mes = input('Diga-me, o mês que você nasceu: ')
ano = input('Diga-me, o ano que você nasceu: ')
print('De acordo com os dados informados, você nasceu na data de {}/{}/{} .Está correto?'.format(dia, mes, ano))
