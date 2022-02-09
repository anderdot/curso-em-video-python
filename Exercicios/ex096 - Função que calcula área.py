# Desafio 096: Faça um programa que tenha uma função chamada área(), que receba 
# as dimensões de um terreno retangular (largura e comprimento) e mostre a área 
# do terreno.
from rotinas import var, titulo

def area(largura, comprimento):
    print(f'A área do terreno é de {var(largura * comprimento)} metros².')

titulo('Calcular a área de um terreno', 60)
l = float(input('Digite a largura (metros): '))
c = float(input('Digite o comprimento (metros): '))
area(l, c)
