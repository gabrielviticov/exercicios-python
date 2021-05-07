'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade_car = int(input('Informe a velocidade atual do carro: '))
multa = (velocidade_car - 80) * 7.0
if velocidade_car > 80:
    print('VOCÊ FOI MULTADO! Pois ultrapassou o limite de velocidade permitido, que é 80KM/H.')
    print('VOCÊ DEVE PAGAR UMA MULTA NO VALOR DE R${:.2f}'.format(multa))
else:
    print('Você não ultrapassou o limite permitido. Continue dirigindo com segurança!')
