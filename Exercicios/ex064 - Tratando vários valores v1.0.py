# Desafio 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando a flag).
from cores import cor

cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para sair]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print('Você digitou {1}{2}{0} números e a soma foi {1}{3}{0}.'.format(
    cor.reset,
    cor.verde,
    cont,
    soma
))
