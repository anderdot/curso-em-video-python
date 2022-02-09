# Desafio 098: Faça um programa que tenha uma função chamada contador(), que 
# receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from rotinas import var, titulo
from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {var(inicio)} a {var(fim)} de {var(passo)} em {var(passo)}.')
    if passo == 0:
        passo = 1
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        fim += 1
        if passo < 0:
            passo *= -1
    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True) # evita o buffer de tela
        sleep(0.2)
    print()
    titulo('Fim da contagem', 30)


contador(1, 10, 1)
contador(10, 0, 2)
titulo('Sua vez', 30)
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
