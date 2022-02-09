# Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e os
# guarde em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
from cores import cor

numeros = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: ')),
)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {cor.verde}{numeros.count(9)}{cor.reset} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {cor.verde}{numeros.index(3) + 1}ª{cor.reset} posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'O valores pares digitados foram: ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(f'{cor.verde}{n}{cor.reset}', end = ' ')
