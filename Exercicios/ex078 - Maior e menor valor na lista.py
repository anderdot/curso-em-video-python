# Desafio 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma
# lista. No final, mostre qual foi o maior e menor valor digitado e suas respectivas
# posições na lista. 
from cores import cor

numeros = []
menor = maior = 0 
for i in range(0,5):
    numeros.append(int(input(f'Digite o número da posição {i + 1}: ')))
    if i == 0:
        menor = maior = numeros[i]
    else:
        menor = min(numeros[i], menor)
        maior = max(numeros[i], maior)

print('-==-' * 10)
print(f'A lista digitada foi: {numeros}')
print(f'O menor valor foi {cor.verde}{menor}{cor.reset}. Nas posições ', end = f'{cor.verde}')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i + 1}', end = ' ')
print(cor.reset)
print(f'O maior valor foi {cor.verde}{maior}{cor.reset}. Nas posições ', end = f'{cor.verde}')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i + 1}', end = ' ')
print(cor.reset)
