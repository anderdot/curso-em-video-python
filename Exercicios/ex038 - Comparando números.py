# Desafio 038: Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela a mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
from cores import cor

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
if n1 > n2:
    print('O {}primeiro{} é maior.'.format(cor.verde, cor.reset))
elif n2 > n1:
    print('O {}segundo{} é maior.'.format(cor.verde, cor.reset))
else:
    print('Não existe valor maior, os dois são {}iguais{}'.format(cor.verde, cor.reset))
