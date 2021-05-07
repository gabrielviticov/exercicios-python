'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

altura = float(input('Informe a sua altura (metros): '))
peso = float(input('Informe o seu peso (kg): '))
imc = peso / (altura**2)
print('Você possui um IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você se encontra: ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você se encontra: PESO IDEAL')
elif imc >= 25 and imc <= 30:
    print('Você se encontra: SOBREPESO')
elif imc >= 30 and imc <= 40:
    print('Você se encontra: OBESIDADE')
else:
    print('Você se encontra: OBESIDADE MÓRBIDA')
