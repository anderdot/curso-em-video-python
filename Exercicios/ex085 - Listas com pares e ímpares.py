# Desafio 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separado os pores dos ímpares.
# No final, mostre os valores pares e ímpares em forma crescente. 
from cores import cor

numeros = [[],[]]

for i in range(0, 7):
    numero = int(input(f'Digite o {str(i + 1)}º número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'{" Resultado ":-^30}')
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {cor.verde}{numeros[0]}{cor.reset}.')
print(f'Os números ímpares são {cor.verde}{numeros[1]}{cor.reset}.')
