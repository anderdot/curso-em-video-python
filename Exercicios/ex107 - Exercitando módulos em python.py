# Desafio 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe 
# esse módulo e use algumas dessas funções.
from rotinas import var, titulo
from modulos.ex107 import moeda

valor = int(input('Digite um valor: R$ '))
titulo('Análise')
print(f'A metade de R$ {var(valor)} é R$ {var(moeda.metade(valor))}.')
print(f'O dobro de R$ {var(valor)} é R$ {var(moeda.dobro(valor))}.')
print(f'A taxa de 10% de R$ {var(valor)} é R$ {var(moeda.aumentar(valor, 10))}.')
print(f'O desconto de 15% de R$ {var(valor)} é R$ {var(moeda.diminuir(valor, 15))}.')
