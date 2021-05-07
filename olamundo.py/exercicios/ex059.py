'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Qual é a opção? '))
    if escolha == 1:
        print('A soma entre {} + {} = {}'.format(p1, p2, p1+p2))
    elif escolha == 2:
        print('A multiplicação entre {} x {} = {}'.format(p1, p2, p1*p2))
    elif escolha == 3:
        if p1 > p2:
            print('O valor {} é maior que o valor {}'.format(p1, p2))
        else:
            print('O valor {} é maior que o valor {}'.format(p2, p1))
    elif escolha == 4:
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('FIM DO PROGRAMA.')
    else:
        print('Opção inválida. Tente novamente!')
