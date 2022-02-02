# Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. no final
# da execução, mostre a média entre todos os valores e qual foi o maior e menos valor
# lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
# valores. 
from cores import cor

cont = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = numero
    else:
        maior = max(maior, numero)
        menor = min(menor, numero)
    cont += 1
    soma += numero
    resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if resposta == 'N':
        break
print('Você digitou {1}{2}{0} numeros, a média foi {1}{3}{0}, maior número foi {1}{4}{0} e o menor {1}{5}{0}.'.format(
    cor.reset,
    cor.verde,
    cont,
    soma / cont,
    maior,
    menor
))