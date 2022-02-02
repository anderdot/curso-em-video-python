# Desafio 048: Faça um programa que calcule a soma entre todos os números ímpares que
# são múltiplos de três e que se encontra no intervalo de 1 até 500. 
from cores import cor

soma = 0
cont = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        soma += i
        cont += 1
print('O resultado da soma dos {1}{2}{0} número ímpares multiplos de três é {1}{3}{0}.'.format(
    cor.reset,
    cor.verde,
    cont,
    soma
))
