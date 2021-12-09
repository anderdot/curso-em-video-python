# Desafio 006: Crie um algoritmo que leia um número inteiro e mostre seu dobro, 
# triplo e raiz
from cores import cor

n = int(input('Digite um número: '))
print('O dobro é {1}{2}{0}, triplo é {1}{3}{0} e a raiz é {1}{4:.3f}{0}.'.format(
    cor.reset,
    cor.verde,
    n * 2, 
    n * 3, 
    n ** (1/2))) #raiz
