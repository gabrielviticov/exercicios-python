'''
Estrutura Condicional
Condições simples e compostas:

IF/ELSE - Se/Senão - Para condição verdadeira IF - Para condição falsa ELSE

if (condição):
    comando1
    comando2
    comando3
else:
    comando1
    comando2
    comando3

ex:
carro_idade = int(input('Quantos anos tem seu carro? '))
if carro_idade <= 3:
    print('Olha, seu carro ainda é novo!')
else:
    print('Olha, seu carro já está ficando velho!')

ex:
nome = str(input('Digite seu nome: '))
if nome == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Que nome comum!')
print('Bom dia {}!'.format(nome))

ex:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m >= 5.0:
    print('Aprovado!')
else:
    print('Reprovado!')
print('Sua média é {:.2f}'.format(m))
'''