'''
Condições aninhadas:
    É uma estrutura condicional dentro de uma estrututra condicional
    Como vimos anteriormente - IF/ELSE são condições compostas
    IF - bloco verdadeiro
    ELSE - bloco falso

    Na estrutura condicionaç aninhada é possível usar um IF dentro de um ELSE: ELIF - (Else If)
    Sendo esses ELIF, uma condição aninhada.
    Outra coisa muito importante na estrutura ELIF - é a sua condição, ele leva a mesma característica do IF. ex:

    a = int(input('Digite a sua idade: '))
    if idade > 18:
        comando1
        comando2
        comando3
    elif idade >= 16:
        comando1
        comando2
        comando3
    else:
        comando1
        comando2
        comando3

    Como você pode ver, o elif também é necessário expecifícar a condição para que ele seja executado. Uma coisa
    muito interessante a ser observada: o elif não funciona sem o if, e quando você decide utilizar o elif,
    o else se torna opcional. 

    ex:
    nome = str(input('Digite seu primeiro nome: ')).title()
if nome == 'Gabriel':
    print('\nQue nome bonito você tem!')
elif nome == 'Kelly' or nome == 'Antonia' or nome == 'Petros' or nome == 'Sonia' or nome == 'Aristides':
    print('\nQue nome lindo você tem ')
else:
    print('\nQue nome comum você tem!')
'''

nome = str(input('Digite seu primeiro nome: ')).title()
if nome == 'Gabriel':
    print('\nQue nome bonito você tem!')
elif nome == 'Kelly' or nome == 'Antonia' or nome == 'Petros' or nome == 'Sonia' or nome == 'Aristides':
    print('\nQue nome lindo você tem ')
elif nome in 'Amanda Ana Julia Barbara':
    print('\nVocê tem um belo nome feminino!')
else:
    print('\nQue nome comum você tem!')