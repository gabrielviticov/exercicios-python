# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: U$1.00 == R$5.58

money = float(input('Diga-me, quantos reais você tem na sua carteira R$'))
dollar = money/5.58
print('Como você possui R${:.2f}\nPoderá comprar até U${:.2f}'.format(money, dollar))
