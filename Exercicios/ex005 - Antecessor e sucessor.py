# Desafio 005: Faça um programa que leia um número inteiro e mostre o seu 
# antecessor e sucessor.
from cores import cor

numero = int(input('Digite um número: '))
print('{1}{4}{0} < {2}{5}{0} > {3}{6}{0}'.format(
    cor.reset,    #0
    cor.vermelho, #1
    cor.azul,     #2
    cor.verde,    #3  
    numero - 1,   #4
    numero,       #5
    numero + 1))  #6
