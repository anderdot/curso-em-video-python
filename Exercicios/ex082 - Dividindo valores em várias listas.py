# Desafio 082: Crie um programa que vai ler vários números e colocar em uma list.
# Depois disso, crie duas listas extras que vão conter apenas valores pares e os
# valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
from cores import cor

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        escolha = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('-==-' * 10)
print(f'Todos os números são {cor.verde}{numeros}{cor.reset}')
print(f'Todos os números pares são {cor.verde}{pares}{cor.reset}')
print(f'Todos os números ímpares são {cor.verde}{impares}{cor.reset}')
