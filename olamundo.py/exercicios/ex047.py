'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

#for cont in range(1, 51):
#    if cont % 2 == 0:
#        print('{:02}'.format(cont), end=' ')
#print('FIM')
# A forma apresentada acima não está errada! Porém, ela gasta mais o processador da máquina. Pois ela invés de fazer apenas uma operação contínua ela acabou fazendo duas.

for cont in range(2, 51, 2):
    print('{:02}'.format(cont), end=' ')
print('FIM')
# Essa forma é mais otimizada que a anterior, pois ela não precisa fazer mais de uma operação, enquanto a outra fazia duas. Acarretando em um processador com mais trabalho. 