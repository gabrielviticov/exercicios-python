'''
ex029: Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

from colorise import set_color, reset_color
cor = {
    'limpa':'\033[m',
    'white':'\033[1;97m'
}
set_color(fg='green')
velocidade_carro = int(input('Informe a velocidade do carro KM/H: '))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7.00
    print('\nMULTADO! VOCÊ ULTRAPASSOU O LIMITE PERMITIDO. LOGO TERÁ QUE PAGAR ', end='')
    reset_color()
    print('{}R${:.2f}{}'.format(cor['white'], multa, cor['limpa']))
else:
    set_color(fg='green')
    print('\nCONTINUE ASSIM. DIRIGINDO COM SEGURANÇA!')
