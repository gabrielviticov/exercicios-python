'''
ex031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
'''

from colorise import set_color, reset_color
cor = {
    'limpa':'\033[m',
    'white_bold':'\033[1;97m'
}
set_color(fg='green')
distancia_km = int(input('Informe a distância da viagem KM: '))
print('\nVocê está prestes a iniciar uma viagem de {}{}KMs{}'.format(cor['white_bold'], distancia_km, cor['limpa']))
reset_color()
if distancia_km <= 200:
    preco = distancia_km * 0.50
    set_color(fg='green')
    print('O preço a se pagar é de {}R${:.2f}{}'.format(cor['white_bold'], preco, cor['limpa']))
else:
    set_color(fg='green')
    preco = distancia_km * 0.45
    print('O preço a se pagar é de {}R${:.2f}{}'.format(cor['white_bold'], preco, cor['limpa']))
