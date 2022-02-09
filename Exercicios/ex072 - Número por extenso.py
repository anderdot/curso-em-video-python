# Desafio 072: Olá mundo 3 > Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (ente 0 e 20) e mostra-lo 
# por extenso.
from cores import cor

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número: '))
    if numero in range(0, 20):
        break
print(f'Você digitou {cor.verde}{numeros[numero]}{cor.reset}.')
    