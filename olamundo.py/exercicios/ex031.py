'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

viagem = float(input('Informe a distância da viagem em KM: '))
if viagem <= 200:
    viagem_curta = viagem * 0.50
    print('A sua viagem tem {}KM\nÉ considerada uma viagem de curta distância. Você deverá pagar R${:.2f}'.format(viagem, viagem_curta))
else:
    viagem_longa = viagem * 0.45
    print('A sua viagem tem {}KM\nÉ considerada uma viagem de longa distância. Você deverá pagar R${:.2f}'.format(viagem, viagem_longa))
print('{}'.format('boa viagem'.upper()))
