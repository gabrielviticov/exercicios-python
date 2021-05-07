'''
Aula bônus: Cores no terminal

Código ANSI para cores: \033[0;00;00m
(as sequências de 00 separadas pelo ponto-vírgula é a representação das cores em Python
a primera sequência da 0 diz respeito ao estilo, se ela é normal, negrito, itálico. A segunda sequência diz respeito à cor do texto
e por último temos o background)

Lista de comandos:
Style:                      text:                       background: (segue a mesma lógica de cores, porém indo do 40 ao 47)
[ 0 - padrão ]              [ 30 - Branco ]
[ 1 - negrito ]             [ 31 - Vermelho ]
[ 4 - underline ]           [ 32 - Verde ]
[ 7 - inverter cores ]      [ 33 - Amarelo ]
                            [ 34 - Azul ]
                            [ 35 - Roxo ]
                            [ 36 - Ciano ]
                            [ 37 - Cinza ]

ex:
nome = input('Como gostaria de ser chamado? ')
print('Prazer em te conhecer {}{}{}!'.format('\033[1;36m', nome, '\033[m'))


ex:
idade = int(input('Digite a sua idade: '))
cores = {
    'limpa':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31;',
    'ciano':'\033[36m'
}
print('Você tem {}{}{} anos de idade'.format(cores['amarelo'], idade, cores['limpa'], ))
'''

import colorise
