# Desafio 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, ja na posição correta de inserção (sem usar sort()).
# No final, mostre a lista ordenada na tela.
from cores import cor

numeros = []
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    if i == 0 or numero > numeros[len(numeros) - 1]: # ou numeros[-1]
        print(f'Adicionado na {cor.verde}última{cor.reset} posição.')
        numeros.append(numero)
    else:
        for j in range(0, len(numeros)):
            if numero <= numeros[j]:
                numeros.insert(j, numero)
                print(f'Adicionado na posição {cor.verde}{j + 1}{cor.reset}.')
                break
            j += 1
print('-==-' * 10)
print(f'Os números digitados em ordem foram {cor.verde}{numeros}{cor.reset}.')
