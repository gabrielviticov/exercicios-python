'''
O índice de massa corpórea de uma pessoa (IMC) é dado pelo seu peso (em quilogramas) dividido pelo quadrado de sua altura (em metros). Faça um programa em PYTHON que leia o peso e altura de uma pessoa. Informe a sua situação, de acordo com os critérios a seguir:

IMC <= 18,5 --> Magro
IMC > 18.5 e IMC <= 25.0 --> Normal
IMC > 25.0 e IMC <= 30.0 --> Sobrepeso
IMC > 30.0 --> Obeso
'''

peso = float(input('Informe o seu peso atual: '))
altura = float(input('Informe a sua altura atual: '))
imc = peso / (altura**2)
if imc <= 18.5:
    print('MAGRO')
elif imc > 18.5 and imc <= 25.0:
    print('NORMAL')
elif imc > 25.0 and imc <= 30.0:
    print('SOBREPESO')
elif imc > 30.0:
    print('OBESO')
print('O seu IMC é de {:.1f}'.format(imc))
