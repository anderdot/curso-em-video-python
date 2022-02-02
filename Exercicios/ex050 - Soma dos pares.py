# Desafio 050: Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o 
from cores import cor

soma = 0
cont = 0
for i in range(0, 6):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Informado os {1}{2}{0} números pares a soma deu {1}{3}{0}.'.format(
    cor.reset,
    cor.verde,
    cont,
    soma
))
