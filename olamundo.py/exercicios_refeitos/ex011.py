'''
ex011:  Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de
tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''

largura = float(input('Informe a largura de uma parede: '))
altura = float(input('Informe a altura de uma parede: '))
area = largura * altura
tinta = area / 2
cores = {
    'limpa':'\033[m',
    'ciano':'\033[1;36m'
}
print('Sua parede tem a dimensão de {}{} x {}{} e sua área é de {}{}m²{}.'.format(cores['ciano'] ,largura, altura, cores['limpa'], cores['ciano'],area, cores['limpa']))
print('Para pintar essa parede, você precisará de {}{:.2f}l{} de tinta.'.format(cores['ciano'], tinta, cores['limpa']))
