# Desafio 100: Faça um programa que tenha uma lista chamada números e duas 
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 
# números e vai colocá-los dentro da lista e a segunda função vai mostrar a 
# soma entre todos os valores pares sorteados pela função anterior.
from rotinas import var, titulo
from random import randint

def sortear(lista):
    titulo('Gerando números', 30)
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Números: {var(lista)}')


def somarPar(lista):
    titulo('Somando os pares', 30)
    soma = 0
    print('A soma dos números', end=' ')
    for n in lista:
        if n % 2 == 0:
            soma += n
            print(var(n), end=' ')
    print(f'é {var(soma)}.')


lista = []
sortear(lista)
somarPar(lista)
