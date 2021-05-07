# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Informe um número inteiro: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('De acordo com o número digitado: {}'.format(num))
print('O seu dobro é: {}'.format(dobro))
print('O triplo é: {}'.format(triplo))
print('E a sua raíz quadrada é: {:.2f}'.format(raiz))
