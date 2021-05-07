'''
ex005: faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
'''

num = int(input('Digite um número inteiro: '))
print('O número digitado foi: {}{}{}'.format('\033[1;34m', num, '\033[m'))
print('O seu sucessor é: {}{}{}'.format('\033[1;31m', num+1, '\033[m'))
print('O seu antecessor é: {}{}{}'.format('\033[1;31m', num-1, '\033[m'))
