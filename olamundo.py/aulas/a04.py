'''
Manipulação de string

frase = 'Curso em Vídeo Python'
dentro da variável "frase" temos mini-espaços para serem preenchido pelo valor da variável, no caso, Curso em video Python
[C][u][r][s][o][][e][m][][V][í][d][e][o][][P][y][t][h][o][n]
cada mini-espaços vai receber um indíce - uma sequência númerica começando pelo número 0 e indo até o n

Técnica de fatiamento de strings:
    frase = 'Curso em Vídeo Python'  - dentro da memoria - [C][u][r][s][o][][e][m][][V][í][d][e][o][][P][y][t][h][o][n]
    frase[9] - ele retornará o caractere de indíce 9, no caso, a letra "V"
    frase[9:13] - ele retornará um conjunto de caracteres entre o indíce 9 ao 13 - "Víde"
    frase[9:21] - ele retornará um conjunto de caracteres entre o indice 9 até o 21 - "Video Python"
    frase[9:21:2] - ele retornará os seguintes critérios - ele primeiro irá começar do indíce 9, segundo ele terminará no indíce 21, e esse 2 ele irá pular em dois em dois - "VdoPto"
    frase[:5] - ele começará pelo indíce 0 e irá até o indíce 5 - "Curso"
    frase[15:] - ele começará pelo indíce 15 e irá até o final, no caso, até o indice final - "Python"
    frase[9::3] - ele começará pelo indíce 9 e irá até o final em três em três - "VePh"

Técnica de Análise de strings:
    len(frase) - mostra o comprimento de uma string
    frase.count('o') - ele irá contar quantas vezes aparece a letra 'o' dentro de uma string
    frase.count('o',0,13) - ele irá contar quantas vezes aparece a letra 'o' junto com o fatiamento
    frase.find('deo') - ele irá procurar o conjunto de caracteres e após isso ele retornará o valor de sua localização, no caso, em que indíce começa esse conjunto de caracteres
    frase.find('Android') - note que a variável não possui nenhum conjunto de caraceteres igual à 'Android', logo ele irá retornar o valor -1 de "não encontrado"
    'Curso' in frase - dentro da variável frase existe um conjunto de caracteres igual à 'Curso'? esse parâmentro irá retornar apenas dois valores: True ou False

Técnica de transformação de string:
    frase.replace('Python', 'Android') - primeiro ele irá procurar pelo conjunto 'Python' e depois irá substituir por 'Android'
    frase.upper() - Esse método irá modificar a string inteira, ele irá coloca-la toda em maiúscula, o que já estiver em maiúsculo, ele não modificará
    frase.lower() - Esse método é semelhante ao anterior, só que ele transforma a string inteira em minúscula
    frase.capitalize() - Esse método é semelhante aos anteriores, só que ele vai deixar somente o caracter de indíce 0 em letra maiúscula, o resto todo em minúsculo
    frase.title() - Ele é bem semelhante ao capitalize - porém ele é mais aprofundado - tudo o que estiver espaço, a próxima letra ela será capitalizada, ou seja, ela estará em maiúscula
    frase.strip() - Veja, esse método é muito importânte no rumo da tecnologia - ele elimina os espaços excendentes digitados pelo usuário
        isso é muito comum no ramo - quando a pessoa mais leiga preenche um formulário, ela geralmente aperta diversas vezes a tecla de espaço
        para ver se está funcionando - o método strip() serve para eliminar esses espaços desnecessários e não comprometer as funcionalidades do programa
    frase.rstrip() - Mesma coisa que a anterior, só que ele irá apenas eliminar os espaços excendentes da direita
    frase.lstrip() - Mesma coisa que a anterior, só que ele irá apenas eliminar os espaços excendentes da esquerda

Técnica de divisão de strings:
    frase.split() - Ele divide os espaços ex: 'Curso em Vídeo Python' tudo o que for considerado espaço ele irá dividir em: [Curso] [em] [Vídeo] [Python]. Essa divisão
        faz com que o indíce recomece. Tecnicamente esse split irá gerar uma lista com todas essas palavras e um indíce com todos esses blocos: [Curso] indíce 0
        [em] indíce 1 - [Vídeo] = 2 - [Python] = 3 . Esse split ele divide uma string em lista

frase = 'Curso em Vídeo Python'
conjunto = frase.split()
print(conjunto[1])

Técnica de junção de strings:
    '-'.join(frase) - Vamos supor que você fez o comando frase.split() e nisso foi gerado uma lista. O join serve para juntar essa lista em uma string única.
        Sendo que agora ela irá apresentar o '-' como separador de espaços - mas mesmo assim é uma string única.
'''

