'''
Operadores aritméticos:
    adição +
    subtração -
    multiplicação *
    divisão /
    exponenciação ** pow(base, exponente) ex: pow (4, 2)
    divisão inteira //
    resto da divisão %

Ordem de precedência:
    1º parentêses ()
    2º exponenciação **
    3º multiplicação, divisão, divisão inteira e resto da divisão * / // %
    4º adição e subtração + -

dicas: para calculo de raíz quadrada, você pode usar esse calculo: num**(1/2) ex: raíz quadrada de 81; 81**(1/2)
        para o calculo da raíz cúbica, você usa: num**(1/3)
    para potenciação, você pode usar uma função interna: pow(base, expoente) ex: pow(4, 2)

ex:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
soma = n1 + n2
sub = n1 - n2
mu = n1 * n2
div = n1 / n2
di = n1 // n2
re = n1 % n2
ex = n1 ** n2
print('A soma entre {} + {} = {}'.format(n1, n2, soma))
print('A subtração entre {} - {} = {}'.format(n1, n2, sub))
print('A multiplicação entre {} x {} = {}'.format(n1, n2, mu))
print('A divisão entre {} / {} = {:.2f}'.format(n1, n2, div))
print('A divisão inteira entre {} // {} = {}'.format(n1, n2, di))
print('O resto da divisão entre {} % {} = {}'.format(n1, n2, re))
print('A exponenciação entre {} ** {} = {}'.format(n1, n2, ex))

'''

