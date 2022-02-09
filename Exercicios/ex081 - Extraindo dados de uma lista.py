# Desafio 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e esta ou não na lista. 
from cores import cor

numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print(f'Foram digitados {cor.verde}{len(numeros)}{cor.reset} números.')
numeros.sort(reverse = True)
print(f'Os números em ordem decrescente são {cor.verde}{numeros}{cor.reset}.')
if 5 in numeros:
    print(f'O número 5 foi digitado {cor.verde}{numeros.count(5)}{cor.reset} vez(es).')
else:
    print('O número 5 não foi digitado nenhuma vez.')
