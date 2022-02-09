# Desafio 099: Faça um programa que tenha uma função chamada maior(), que receba 
# vários parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.
from rotinas import var, titulo

def maior(*numeros):
    titulo('', 30)
    print(f'O maior valor é {var(max(numeros))}')


maior(0, 1, 1, 2, 3, 5, 8)
maior(4, 6, 8, 10)
maior(7, 1)
